
#!/usr/bin/env python3
"""
MP3 Downloader (GUI)

A simple, user-friendly button-based app to download MP3s for offline use,
tag them (ID3), create manifests, and optionally zip the results.

- Paste URLs or load from a file
- Pick an output folder
- (Optional) Fill in tags & select cover art
- Click "Start Download"

Dependencies:
    pip install mutagen
"""
import os
import re
import json
import csv
import sys
import zipfile
import hashlib
import tempfile
import threading
import queue
import urllib.request
import urllib.error
from urllib.parse import urlparse, unquote
from concurrent.futures import ThreadPoolExecutor, as_completed

# GUI
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Optional dependency check (ID3 tagging)
try:
    from mutagen.easyid3 import EasyID3
    from mutagen.id3 import ID3, APIC, ID3NoHeaderError
    from mutagen.mp3 import MP3
    HAVE_MUTAGEN = True
except Exception:
    HAVE_MUTAGEN = False

# ---------------- Core helpers ----------------

def sanitize_filename(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def filename_from_cd(cd_header: str | None) -> str | None:
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

def sha256_file(path: str, chunk_size: int = 1024*1024) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk_size)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def write_id3(path: str, tags: dict, artwork_path: str | None, log):
    if not HAVE_MUTAGEN:
        log("[tag] Mutagen not installed; skipping tags")
        return
    # EasyID3 for common fields
    try:
        audio = EasyID3(path)
    except ID3NoHeaderError:
        audio = MP3(path)
        audio.add_tags()
        audio = EasyID3(path)

    mapping = {"title":"title","artist":"artist","album":"album","genre":"genre","comment":"comment"}
    for k, v in mapping.items():
        if tags.get(k) not in (None, ""):
            audio[v] = [str(tags[k])]
    if tags.get("track") not in (None, ""):
        audio["tracknumber"] = [str(tags["track"])]
    if tags.get("year") not in (None, ""):
        audio["date"] = [str(tags["year"])]
    audio.save()

    if artwork_path and os.path.exists(artwork_path):
        try:
            id3 = ID3(path)
            with open(artwork_path, "rb") as imgf:
                img_bytes = imgf.read()
            id3.add(APIC(encoding=3, mime="image/jpeg", type=3, desc="Cover", data=img_bytes))
            id3.save()
        except Exception as e:
            log(f"[tag] Failed to embed artwork: {e}")

def download_one(url: str, out_dir: str, opts, log) -> dict:
    headers = {
        "User-Agent": opts["user_agent"],
        "Accept": "*/*",
    }
    attempt = 0
    last_err = None
    while attempt <= opts["retries"]:
        attempt += 1
        req = urllib.request.Request(url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=opts["timeout"]) as resp:
                content_type = resp.headers.get("Content-Type", "")
                cd = resp.headers.get("Content-Disposition")
                if opts["verify_mime"] and content_type:
                    if not content_type.lower().startswith("audio"):
                        return {"url": url, "status": "error", "path": None, "bytes": None,
                                "error": f"Unexpected content type: {content_type}",
                                "content_type": content_type or None, "sha256": None}
                name = filename_from_cd(cd) or default_name_from_url(url)
                final_path = unique_path(out_dir, name)

                bytes_written = 0
                with tempfile.NamedTemporaryFile("wb", delete=False, dir=out_dir) as tmp:
                    tmp_path = tmp.name
                    while True:
                        chunk = resp.read(opts["chunk_size"])
                        if not chunk:
                            break
                        tmp.write(chunk)
                        bytes_written += len(chunk)
                os.replace(tmp_path, final_path)

                checksum = sha256_file(final_path)

                # Tags
                if opts["tags"] or opts["artwork"]:
                    try:
                        write_id3(final_path, opts["tags"], opts["artwork"], log)
                    except Exception as e:
                        log(f"[tag] Failed to write tags: {e}")

                return {"url": url, "status": "ok", "path": final_path, "bytes": bytes_written,
                        "error": None, "content_type": content_type or None, "sha256": checksum}
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as e:
            last_err = str(e)
            log(f"[retry] {url}: {last_err} (attempt {attempt}/{opts['retries']+1})")
    return {"url": url, "status": "error", "path": None, "bytes": None, "error": last_err or "Unknown error",
            "content_type": None, "sha256": None}

def write_manifest(results: list[dict], out_dir: str) -> tuple[str, str, str]:
    os.makedirs(out_dir, exist_ok=True)
    manifest_json = os.path.join(out_dir, "manifest.json")
    manifest_csv = os.path.join(out_dir, "manifest.csv")
    checksums_out = os.path.join(out_dir, "checksums.json")

    with open(manifest_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    fields = ["url","status","path","bytes","content_type","sha256","error"]
    with open(manifest_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in results:
            w.writerow({k: r.get(k) for k in fields})
    checksums_map = {r["url"]: r["sha256"] for r in results if r["status"] == "ok" and r.get("sha256")}
    with open(checksums_out, "w", encoding="utf-8") as f:
        json.dump(checksums_map, f, indent=2)

    return manifest_json, manifest_csv, checksums_out

def make_zip(zip_out: str, files: list[str], extras: list[tuple[str, str]]):
    os.makedirs(os.path.dirname(os.path.abspath(zip_out)) or ".", exist_ok=True)
    with zipfile.ZipFile(zip_out, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for f in files:
            if f and os.path.exists(f):
                z.write(f, arcname=os.path.basename(f))
        for p, arcname in extras:
            if p and os.path.exists(p):
                z.write(p, arcname=arcname)

# ---------------- GUI App ----------------

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MP3 Downloader (Offline)")
        self.geometry("900x650")
        self.minsize(820, 580)

        self.queue = queue.Queue()
        self.downloading = False

        self._build_ui()
        self._poll_log_queue()

    def _build_ui(self):
        pad = 6

        # URLs frame
        urls_frame = ttk.LabelFrame(self, text="MP3 URLs")
        urls_frame.pack(fill="both", expand=False, padx=pad, pady=(pad, 0))

        self.urls_text = tk.Text(urls_frame, height=6, wrap="word")
        self.urls_text.pack(side="left", fill="both", expand=True, padx=(pad,0), pady=pad)

        btns_url = ttk.Frame(urls_frame)
        btns_url.pack(side="right", fill="y", padx=pad, pady=pad)
        ttk.Button(btns_url, text="Load URLs from File...", command=self.load_urls_file).pack(fill="x", pady=(0,4))
        ttk.Button(btns_url, text="Clear URLs", command=lambda: self.urls_text.delete("1.0", "end")).pack(fill="x")

        # Output frame
        out_frame = ttk.LabelFrame(self, text="Output")
        out_frame.pack(fill="x", padx=pad, pady=pad)

        self.out_dir_var = tk.StringVar(value=os.path.abspath("./offline_mp3s"))
        ttk.Label(out_frame, text="Output folder:").grid(row=0, column=0, sticky="w", padx=pad, pady=pad)
        ttk.Entry(out_frame, textvariable=self.out_dir_var).grid(row=0, column=1, sticky="we", padx=(0, pad), pady=pad)
        ttk.Button(out_frame, text="Choose...", command=self.choose_out_dir).grid(row=0, column=2, padx=(0, pad), pady=pad)

        out_frame.columnconfigure(1, weight=1)

        # Tags frame
        tags = ttk.LabelFrame(self, text="ID3 Tags (Optional, applied to all)")
        tags.pack(fill="x", padx=pad, pady=pad)

        self.title_var = tk.StringVar()
        self.artist_var = tk.StringVar()
        self.album_var = tk.StringVar()
        self.genre_var = tk.StringVar()
        self.comment_var = tk.StringVar()
        self.track_var = tk.StringVar()
        self.year_var = tk.StringVar()
        self.artwork_var = tk.StringVar()

        row = 0
        ttk.Label(tags, text="Title").grid(row=row, column=0, sticky="w", padx=pad, pady=pad)
        ttk.Entry(tags, textvariable=self.title_var).grid(row=row, column=1, sticky="we", padx=(0, pad), pady=pad)
        ttk.Label(tags, text="Artist").grid(row=row, column=2, sticky="w", padx=pad, pady=pad)
        ttk.Entry(tags, textvariable=self.artist_var).grid(row=row, column=3, sticky="we", padx=(0, pad), pady=pad)

        row += 1
        ttk.Label(tags, text="Album").grid(row=row, column=0, sticky="w", padx=pad, pady=pad)
        ttk.Entry(tags, textvariable=self.album_var).grid(row=row, column=1, sticky="we", padx=(0, pad), pady=pad)
        ttk.Label(tags, text="Genre").grid(row=row, column=2, sticky="w", padx=pad, pady=pad)
        ttk.Entry(tags, textvariable=self.genre_var).grid(row=row, column=3, sticky="we", padx=(0, pad), pady=pad)

        row += 1
        ttk.Label(tags, text="Comment").grid(row=row, column=0, sticky="w", padx=pad, pady=pad)
        ttk.Entry(tags, textvariable=self.comment_var).grid(row=row, column=1, sticky="we", padx=(0, pad), pady=pad)
        ttk.Label(tags, text="Track #").grid(row=row, column=2, sticky="w", padx=pad, pady=pad)
        ttk.Entry(tags, textvariable=self.track_var).grid(row=row, column=3, sticky="we", padx=(0, pad), pady=pad)

        row += 1
        ttk.Label(tags, text="Year").grid(row=row, column=0, sticky="w", padx=pad, pady=pad)
        ttk.Entry(tags, textvariable=self.year_var).grid(row=row, column=1, sticky="we", padx=(0, pad), pady=pad)
        ttk.Label(tags, text="Artwork (JPEG)").grid(row=row, column=2, sticky="w", padx=pad, pady=pad)
        artwork_row = ttk.Frame(tags)
        artwork_row.grid(row=row, column=3, sticky="we", padx=(0, pad), pady=pad)
        ttk.Entry(artwork_row, textvariable=self.artwork_var).pack(side="left", fill="x", expand=True)
        ttk.Button(artwork_row, text="Browse...", command=self.choose_artwork).pack(side="left", padx=(4,0))

        for c in (1,3):
            tags.columnconfigure(c, weight=1)

        # Options frame
        opts = ttk.LabelFrame(self, text="Options")
        opts.pack(fill="x", padx=pad, pady=pad)

        self.workers_var = tk.IntVar(value=4)
        self.timeout_var = tk.DoubleVar(value=45.0)
        self.retries_var = tk.IntVar(value=2)
        self.mime_verify_var = tk.BooleanVar(value=True)
        self.zip_enable_var = tk.BooleanVar(value=False)
        self.zip_path_var = tk.StringVar(value=os.path.abspath("./bundle.zip"))
        self.ua_var = tk.StringVar(value="Mozilla/5.0 (compatible; OfflineMP3GUI/1.0)")
        self.chunk_var = tk.IntVar(value=1024*64)

        r = 0
        ttk.Label(opts, text="Parallel downloads").grid(row=r, column=0, sticky="w", padx=pad, pady=pad)
        ttk.Spinbox(opts, from_=1, to=32, textvariable=self.workers_var, width=6).grid(row=r, column=1, sticky="w", padx=(0,pad), pady=pad)

        ttk.Label(opts, text="Timeout (s)").grid(row=r, column=2, sticky="w", padx=pad, pady=pad)
        ttk.Entry(opts, textvariable=self.timeout_var, width=8).grid(row=r, column=3, sticky="w", padx=(0,pad), pady=pad)

        ttk.Label(opts, text="Retries").grid(row=r, column=4, sticky="w", padx=pad, pady=pad)
        ttk.Entry(opts, textvariable=self.retries_var, width=6).grid(row=r, column=5, sticky="w", padx=(0,pad), pady=pad)

        r += 1
        ttk.Checkbutton(opts, text="Verify MIME type is audio/*", variable=self.mime_verify_var).grid(row=r, column=0, columnspan=2, sticky="w", padx=pad, pady=pad)
        ttk.Checkbutton(opts, text="Create ZIP bundle", variable=self.zip_enable_var, command=self._toggle_zip).grid(row=r, column=2, columnspan=2, sticky="w", padx=pad, pady=pad)

        ttk.Label(opts, text="ZIP output").grid(row=r, column=4, sticky="e", padx=(pad,4), pady=pad)
        zip_row = ttk.Frame(opts)
        zip_row.grid(row=r, column=5, sticky="we", padx=(0,pad), pady=pad)
        ttk.Entry(zip_row, textvariable=self.zip_path_var, width=28).pack(side="left", fill="x", expand=True)
        ttk.Button(zip_row, text="Browse...", command=self.choose_zip_path).pack(side="left", padx=(4,0))

        r += 1
        ttk.Label(opts, text="User-Agent").grid(row=r, column=0, sticky="w", padx=pad, pady=pad)
        ttk.Entry(opts, textvariable=self.ua_var).grid(row=r, column=1, columnspan=3, sticky="we", padx=(0,pad), pady=pad)
        ttk.Label(opts, text="Chunk size (bytes)").grid(row=r, column=4, sticky="w", padx=pad, pady=pad)
        ttk.Entry(opts, textvariable=self.chunk_var, width=10).grid(row=r, column=5, sticky="w", padx=(0,pad), pady=pad)

        for c in (1,3,5):
            opts.columnconfigure(c, weight=1)

        # Controls
        controls = ttk.Frame(self)
        controls.pack(fill="x", padx=pad, pady=pad)
        self.start_btn = ttk.Button(controls, text="Start Download", command=self.start_download)
        self.start_btn.pack(side="left")
        ttk.Button(controls, text="Open Output Folder", command=self.open_output_folder).pack(side="left", padx=(8,0))

        # Log output
        log_frame = ttk.LabelFrame(self, text="Log")
        log_frame.pack(fill="both", expand=True, padx=pad, pady=(0, pad))
        self.log_text = tk.Text(log_frame, height=12, wrap="word", state="disabled")
        self.log_text.pack(fill="both", expand=True, padx=pad, pady=pad)

        self._toggle_zip()

    # ------------- UI actions -------------

    def load_urls_file(self):
        path = filedialog.askopenfilename(title="Select URLs file", filetypes=[("Text files","*.txt *.csv"),("All files","*.*")])
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = [ln.strip() for ln in f.readlines() if ln.strip() and not ln.strip().startswith("#")]
            existing = self.urls_text.get("1.0", "end").strip()
            joined = ("\n".join(lines) + ("\n"+existing if existing else "")) if lines else existing
            self.urls_text.delete("1.0", "end")
            self.urls_text.insert("1.0", joined)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load URLs: {e}")

    def choose_out_dir(self):
        d = filedialog.askdirectory(title="Choose output folder", mustexist=False)
        if d:
            self.out_dir_var.set(d)

    def choose_artwork(self):
        p = filedialog.askopenfilename(title="Select cover image (JPEG recommended)", filetypes=[("JPEG images","*.jpg *.jpeg"),("All files","*.*")])
        if p:
            self.artwork_var.set(p)

    def choose_zip_path(self):
        p = filedialog.asksaveasfilename(title="Choose ZIP output", defaultextension=".zip", filetypes=[("ZIP files","*.zip")])
        if p:
            self.zip_path_var.set(p)

    def open_output_folder(self):
        d = self.out_dir_var.get().strip()
        if not d:
            return
        try:
            os.makedirs(d, exist_ok=True)
            if sys.platform.startswith("win"):
                os.startfile(d)  # type: ignore[attr-defined]
            elif sys.platform == "darwin":
                os.system(f'open "{d}"')
            else:
                os.system(f'xdg-open "{d}"')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open folder: {e}")

    def _toggle_zip(self):
        state = "normal" if self.zip_enable_var.get() else "disabled"
        # Enable/disable entry and button inside the zip row by traversing children
        # We know the entry and button are in the last row's last frame; safer: enable all children in Options
        for child in self.children.values():
            pass  # no-op
        # Simple approach: do nothing else; zip path can remain editable

    def log(self, msg: str):
        self.queue.put(msg)

    def _poll_log_queue(self):
        try:
            while True:
                msg = self.queue.get_nowait()
                self.log_text.configure(state="normal")
                self.log_text.insert("end", msg + "\n")
                self.log_text.see("end")
                self.log_text.configure(state="disabled")
        except queue.Empty:
            pass
        self.after(100, self._poll_log_queue)

    def start_download(self):
        if self.downloading:
            return
        urls = [u.strip() for u in self.urls_text.get("1.0", "end").splitlines() if u.strip()]
        if not urls:
            messagebox.showwarning("No URLs", "Please paste at least one MP3 URL or load from a file.")
            return
        out_dir = self.out_dir_var.get().strip()
        if not out_dir:
            messagebox.showwarning("Output folder", "Please choose an output folder.")
            return
        os.makedirs(out_dir, exist_ok=True)

        # Gather options
        tags = {
            "title": self.title_var.get().strip() or None,
            "artist": self.artist_var.get().strip() or None,
            "album": self.album_var.get().strip() or None,
            "genre": self.genre_var.get().strip() or None,
            "comment": self.comment_var.get().strip() or None,
            "track": self.track_var.get().strip() or None,
            "year": self.year_var.get().strip() or None,
        }
        # Normalize ints if present
        if tags["track"]:
            try:
                tags["track"] = int(tags["track"])
            except ValueError:
                pass
        if tags["year"]:
            try:
                tags["year"] = int(tags["year"])
            except ValueError:
                pass

        opts = {
            "user_agent": self.ua_var.get().strip() or "Mozilla/5.0 (compatible; OfflineMP3GUI/1.0)",
            "timeout": float(self.timeout_var.get() or 45.0),
            "retries": int(self.retries_var.get() or 2),
            "verify_mime": bool(self.mime_verify_var.get()),
            "chunk_size": int(self.chunk_var.get() or 65536),
            "tags": tags,
            "artwork": self.artwork_var.get().strip() or None,
        }

        self.downloading = True
        self.start_btn.configure(state="disabled")
        self.log("Starting downloads...")

        t = threading.Thread(target=self._do_downloads_thread, args=(urls, out_dir, opts), daemon=True)
        t.start()

    def _do_downloads_thread(self, urls: list[str], out_dir: str, opts: dict):
        results = []
        try:
            workers = max(1, min(32, int(self.workers_var.get() or 4)))
        except Exception:
            workers = 4

        if workers > 1 and len(urls) > 1:
            self.log(f"Using {workers} parallel workers")
            with ThreadPoolExecutor(max_workers=workers) as pool:
                futs = {pool.submit(download_one, u, out_dir, opts, self.log): u for u in urls}
                for fut in as_completed(futs):
                    r = fut.result()
                    if r["status"] == "ok":
                        self.log(f"[ok] {r['url']} -> {r['path']} ({r['bytes']} bytes)")
                    else:
                        self.log(f"[err] {r['url']} -> {r.get('error')}")
                    results.append(r)
        else:
            for u in urls:
                r = download_one(u, out_dir, opts, self.log)
                if r["status"] == "ok":
                    self.log(f"[ok] {r['url']} -> {r['path']} ({r['bytes']} bytes)")
                else:
                    self.log(f"[err] {r['url']} -> {r.get('error')}")
                results.append(r)

        # Sort results in original URL order
        order = {u:i for i,u in enumerate(urls)}
        results.sort(key=lambda r: order.get(r["url"], 10**9))

        # Manifests
        mj, mc, checks = write_manifest(results, out_dir)
        self.log(f"[info] Wrote manifest: {mj}")
        self.log(f"[info] Wrote manifest: {mc}")
        self.log(f"[info] Wrote checksums: {checks}")

        # ZIP
        if self.zip_enable_var.get():
            zip_path = self.zip_path_var.get().strip() or os.path.join(out_dir, "bundle.zip")
            ok_files = [r["path"] for r in results if r["status"] == "ok" and r.get("path")]
            extras = [(mj, "manifest.json"), (mc, "manifest.csv"), (checks, "checksums.json")]
            make_zip(zip_path, ok_files, extras)
            self.log(f"[info] Wrote ZIP: {zip_path}")

        errors = [r for r in results if r["status"] != "ok"]
        if errors:
            self.log(f"Finished with {len(errors)} error(s). See log/manifests for details.")
            messagebox.showwarning("Done (with errors)", f"Downloads completed with {len(errors)} error(s).")
        else:
            self.log("All downloads completed successfully.")
            messagebox.showinfo("Done", "All downloads completed successfully!")

        self.start_btn.configure(state="normal")
        self.downloading = False

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
