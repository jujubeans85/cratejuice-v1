
#!/usr/bin/env python3
"""
Offline MP3 Fetcher

Features
- Download one or many MP3 URLs (parallel, retries, timeouts)
- MIME-type verification (audio/*)
- Safe streaming to disk (temp file -> atomic rename)
- Unique filenames with .mp3 ensured, or from Content-Disposition
- ID3 tagging via mutagen (artist, album, title, track, year, genre, comment, artwork)
- SHA-256 checksums + optional verification against expected checksums
- Manifest JSON & CSV
- ZIP packaging of downloaded files + manifest + checksums
- Simple CLI

Usage examples
--------------
# Basic: download two URLs into ./mp3s and zip them:
python offline_mp3_fetcher.py https://example.com/song1.mp3 https://example.com/song2.mp3 \
  --out-dir ./mp3s --zip-out ./mp3s_bundle.zip

# From a file of URLs (one per line), add ID3 tags for all:
python offline_mp3_fetcher.py --urls-file urls.txt --out-dir ./mp3s \
  --artist "Various" --album "My Mix" --year 2024 --zip-out ./mix.zip

# Per-URL tags via JSON (mapping URL -> tag dict):
# tags.json:
# {
#   "https://example.com/song1.mp3": {"title": "Song One", "artist": "Alice"},
#   "https://example.com/song2.mp3": {"title": "Song Two", "artist": "Bob", "track": 2}
# }
python offline_mp3_fetcher.py --urls-file urls.txt --out-dir ./mp3s --tags-json tags.json

# Verify checksums from JSON (mapping URL -> sha256 hex):
# checksums.json:
# { "https://example.com/song1.mp3": "abc123...hex...", "...": "..." }
python offline_mp3_fetcher.py --urls-file urls.txt --out-dir ./mp3s --verify-checksums checksums.json

Note
----
Download only content you have rights to save.
"""

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import tempfile
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse, unquote
import urllib.request
import urllib.error

# Optional dependency check
try:
    from mutagen.easyid3 import EasyID3
    from mutagen.id3 import ID3, APIC, ID3NoHeaderError
    from mutagen.mp3 import MP3
    HAVE_MUTAGEN = True
except Exception:
    HAVE_MUTAGEN = False

def debug(msg: str):
    print(msg, flush=True)

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def sanitize_filename(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def filename_from_cd(cd_header: Optional[str]) -> Optional[str]:
    if not cd_header:
        return None
    m = re.search(r'filename\*\s*=\s*[^\'"]*\'\'([^;]+)', cd_header, re.IGNORECASE)
    if m:
        return sanitize_filename(unquote(m.group(1)))
    m = re.search(r'filename\s*=\s*"([^"]+)"', cd_header, re.IGNORECASE)
    if m:
        return sanitize_filename(m.group(1))
    m = re.search(r'filename\s*=\s*([^;]+)', cd_header, re.IGNORECASE)
    if m:
        return sanitize_filename(m.group(1).strip().strip("'"))
    return None

def default_name_from_url(url: str) -> str:
    parsed = urlparse(url)
    name = os.path.basename(parsed.path) or ""
    name = unquote(name)
    if not name or name.strip(".") == "":
        name = "audio.mp3"
    if not name.lower().endswith(".mp3"):
        name += ".mp3"
    return sanitize_filename(name)

def unique_path(base_dir: str, filename: str) -> str:
    root, ext = os.path.splitext(filename)
    candidate = os.path.join(base_dir, filename)
    i = 1
    while os.path.exists(candidate):
        candidate = os.path.join(base_dir, f"{root} ({i}){ext}")
        i += 1
    return candidate

def sha256_file(path: str, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk_size)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def write_id3(path: str, tags: Dict, artwork_path: Optional[str] = None):
    if not HAVE_MUTAGEN:
        debug(f"[tag] Mutagen not installed; skipping tags for {path}")
        return
    # EasyID3 for common fields
    try:
        audio = EasyID3(path)
    except ID3NoHeaderError:
        audio = MP3(path)
        audio.add_tags()
        audio = EasyID3(path)

    mapping = {
        "title": "title",
        "artist": "artist",
        "album": "album",
        "genre": "genre",
        "comment": "comment",
    }
    for k, v in mapping.items():
        if k in tags and tags[k] is not None:
            audio[v] = [str(tags[k])]

    if "track" in tags and tags["track"] is not None:
        audio["tracknumber"] = [str(tags["track"])]

    if "year" in tags and tags["year"] is not None:
        # ID3 uses date or originaldate; EasyID3 supports 'date'
        audio["date"] = [str(tags["year"])]

    audio.save()

    # Add artwork via ID3 full API
    if artwork_path and os.path.exists(artwork_path):
        id3 = ID3(path)
        with open(artwork_path, "rb") as imgf:
            img_bytes = imgf.read()
        id3.add(APIC(encoding=3, mime="image/jpeg", type=3, desc="Cover", data=img_bytes))
        id3.save()

def merge_tags(global_tags: Dict, per_url_tags: Dict, url: str) -> Dict:
    tags = dict(global_tags or {})
    if per_url_tags and url in per_url_tags:
        # per-url overrides
        tags.update(per_url_tags[url] or {})
    return tags

def parse_urls(args) -> List[str]:
    urls = list(args.urls or [])
    if args.urls_file:
        with open(args.urls_file, "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s and not s.startswith("#"):
                    urls.append(s)
    # de-dupe, preserve order
    seen = set()
    out = []
    for u in urls:
        if u not in seen:
            out.append(u)
            seen.add(u)
    return out

def load_json(path: Optional[str]) -> Optional[dict]:
    if not path:
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def download_one(url: str, out_dir: str, opts) -> Dict:
    headers = {
        "User-Agent": opts.user_agent,
        "Accept": "*/*",
    }
    attempt = 0
    last_err = None
    while attempt <= opts.retries:
        attempt += 1
        req = urllib.request.Request(url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=opts.timeout) as resp:
                content_type = resp.headers.get("Content-Type", "")
                cd = resp.headers.get("Content-Disposition")
                if opts.verify_mime and content_type:
                    if not content_type.lower().startswith("audio"):
                        return {
                            "url": url, "status": "error", "path": None, "bytes": None,
                            "error": f"Unexpected content type: {content_type}",
                            "content_type": content_type or None,
                            "sha256": None,
                        }
                name = filename_from_cd(cd) or default_name_from_url(url)
                final_path = unique_path(out_dir, name)

                bytes_written = 0
                with tempfile.NamedTemporaryFile("wb", delete=False, dir=out_dir) as tmp:
                    tmp_path = tmp.name
                    while True:
                        chunk = resp.read(opts.chunk_size)
                        if not chunk:
                            break
                        tmp.write(chunk)
                        bytes_written += len(chunk)
                os.replace(tmp_path, final_path)

                # checksum
                checksum = sha256_file(final_path)

                # optional verify expected checksum
                expected = None
                if opts.verify_checksums and isinstance(opts.verify_checksums, dict):
                    expected = opts.verify_checksums.get(url)
                    if expected and expected.lower() != checksum.lower():
                        return {
                            "url": url, "status": "error", "path": final_path, "bytes": bytes_written,
                            "error": f"Checksum mismatch (expected {expected}, got {checksum})",
                            "content_type": content_type or None,
                            "sha256": checksum,
                        }

                # tags
                per_tags = merge_tags(opts.global_tags, opts.per_url_tags, url)
                if per_tags or opts.artwork:
                    try:
                        write_id3(final_path, per_tags, opts.artwork)
                    except Exception as e:
                        debug(f"[tag] Failed to write tags for {final_path}: {e}")

                return {
                    "url": url,
                    "status": "ok",
                    "path": final_path,
                    "bytes": bytes_written,
                    "error": None,
                    "content_type": content_type or None,
                    "sha256": checksum,
                }
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as e:
            last_err = str(e)
    return {
        "url": url, "status": "error", "path": None, "bytes": None,
        "error": last_err or "Unknown error", "content_type": None, "sha256": None
    }

def write_manifest(results: List[Dict], manifest_json: Optional[str], manifest_csv: Optional[str]):
    if manifest_json:
        with open(manifest_json, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
    if manifest_csv:
        fields = ["url","status","path","bytes","content_type","sha256","error"]
        with open(manifest_csv, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for r in results:
                w.writerow({k: r.get(k) for k in fields})

def zip_outputs(zip_out: str, files: List[str], extras: List[Tuple[str, str]]):
    # extras: list of (path, arcname)
    ensure_dir(os.path.dirname(os.path.abspath(zip_out)) or ".")
    with zipfile.ZipFile(zip_out, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for f in files:
            if f and os.path.exists(f):
                z.write(f, arcname=os.path.basename(f))
        for path, arcname in extras:
            if path and os.path.exists(path):
                z.write(path, arcname=arcname)

def main():
    parser = argparse.ArgumentParser(description="Download MP3s for offline use (+ID3, checksums, zip, manifests).")
    parser.add_argument("urls", nargs="*", help="One or more MP3 URLs.")
    parser.add_argument("--urls-file", help="Path to a file containing URLs (one per line).")
    parser.add_argument("--out-dir", default="./offline_mp3s", help="Output directory.")
    parser.add_argument("--max-workers", type=int, default=4, help="Parallel downloads.")
    parser.add_argument("--timeout", type=float, default=45.0, help="Per-request timeout (seconds).")
    parser.add_argument("--retries", type=int, default=2, help="Retries per URL.")
    parser.add_argument("--no-mime-verify", action="store_true", help="Disable MIME-type verification.")
    parser.add_argument("--chunk-size", type=int, default=1024*64, help="Stream chunk size (bytes).")
    parser.add_argument("--user-agent", default="Mozilla/5.0 (compatible; OfflineMP3Fetcher/2.0)", help="Request User-Agent.")

    # Global tags
    parser.add_argument("--title", help="ID3 title for all tracks (can be overridden per URL).")
    parser.add_argument("--artist", help="ID3 artist for all tracks.")
    parser.add_argument("--album", help="ID3 album for all tracks.")
    parser.add_argument("--genre", help="ID3 genre for all tracks.")
    parser.add_argument("--comment", help="ID3 comment for all tracks.")
    parser.add_argument("--track", type=int, help="ID3 track number for all tracks.")
    parser.add_argument("--year", type=int, help="ID3 year for all tracks.")
    parser.add_argument("--artwork", help="Path to a JPEG cover image to embed.")

    parser.add_argument("--tags-json", help="JSON file mapping URL -> tag dict to override/add per-URL.")
    parser.add_argument("--verify-checksums", help="JSON mapping URL -> expected sha256 (verification).")

    parser.add_argument("--manifest-json", default=None, help="Where to write manifest JSON (optional).")
    parser.add_argument("--manifest-csv", default=None, help="Where to write manifest CSV (optional).")

    parser.add_argument("--zip-out", default=None, help="Write a ZIP with all successful MP3s + manifest(s).")

    args = parser.parse_args()

    ensure_dir(args.out_dir)

    global_tags = {
        "title": args.title,
        "artist": args.artist,
        "album": args.album,
        "genre": args.genre,
        "comment": args.comment,
        "track": args.track,
        "year": args.year,
    }

    per_url_tags = load_json(args.tags_json) or {}
    verify_checksums = load_json(args.verify_checksums) if args.verify_checksums else None

    urls = parse_urls(args)
    if not urls:
        print("No URLs provided. See --help for usage.", file=sys.stderr)
        sys.exit(2)

    class Opts:
        pass
    opts = Opts()
    opts.user_agent = args.user_agent
    opts.timeout = args.timeout
    opts.retries = args.retries
    opts.verify_mime = not args.no_mime_verify
    opts.chunk_size = args.chunk_size
    opts.global_tags = global_tags
    opts.per_url_tags = per_url_tags
    opts.artwork = args.artwork
    opts.verify_checksums = verify_checksums

    results: List[Dict] = []

    if args.max_workers and args.max_workers > 1 and len(urls) > 1:
        debug(f"Starting downloads with {args.max_workers} workers...")
        with ThreadPoolExecutor(max_workers=args.max_workers) as pool:
            futs = {pool.submit(download_one, u, args.out_dir, opts): u for u in urls}
            for fut in as_completed(futs):
                r = fut.result()
                status = r["status"]
                if status == "ok":
                    debug(f"[ok] {r['url']} -> {r['path']} ({r['bytes']} bytes)")
                else:
                    debug(f"[err] {r['url']} -> {r.get('error')}")
                results.append(r)
    else:
        for u in urls:
            r = download_one(u, args.out_dir, opts)
            status = r["status"]
            if status == "ok":
                debug(f"[ok] {r['url']} -> {r['path']} ({r['bytes']} bytes)")
            else:
                debug(f"[err] {r['url']} -> {r.get('error')}")
            results.append(r)

    # Sort results to stable order of input URLs where possible
    url_order = {u:i for i,u in enumerate(urls)}
    results.sort(key=lambda r: url_order.get(r["url"], 1_000_000))

    # Manifests
    manifest_json = args.manifest_json or os.path.join(args.out_dir, "manifest.json")
    manifest_csv = args.manifest_csv or os.path.join(args.out_dir, "manifest.csv")
    write_manifest(results, manifest_json, manifest_csv)
    debug(f"[info] Wrote manifest: {manifest_json}")
    debug(f"[info] Wrote manifest: {manifest_csv}")

    # Checksums JSON of successful outputs
    checksums_out = os.path.join(args.out_dir, "checksums.json")
    checksums_map = {r["url"]: r["sha256"] for r in results if r["status"] == "ok" and r.get("sha256")}
    with open(checksums_out, "w", encoding="utf-8") as f:
        json.dump(checksums_map, f, indent=2)
    debug(f"[info] Wrote checksums: {checksums_out}")

    # Bundle ZIP if requested
    if args.zip_out:
        ok_files = [r["path"] for r in results if r["status"] == "ok" and r.get("path")]
        extras = [
            (manifest_json, "manifest.json"),
            (manifest_csv, "manifest.csv"),
            (checksums_out, "checksums.json"),
        ]
        zip_outputs(args.zip_out, ok_files, extras)
        debug(f"[info] Wrote ZIP: {args.zip_out}")

    # Exit code: 0 if all ok, 1 if any error
    any_error = any(r["status"] != "ok" for r in results)
    sys.exit(1 if any_error else 0)

if __name__ == "__main__":
    main()
