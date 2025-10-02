#!/usr/bin/env python3
"""start.py - StaSh + Flask launcher with TLS, health monitoring, and optional on-failure actions.
Usage: python3 start.py [--cert CERT] [--key KEY] [--domain cratejuice.guru] [--enforce-host] [--on-failure stop|restart|webhook] ...
"""
import sys
import os
import argparse
import importlib
import logging
import threading
import time
import socket
import subprocess

# Try to import optional dependencies with helpful errors
try:
    from stash import stash
except Exception as e:
    raise RuntimeError("Failed to import stash: %s" % e)

try:
    from flask import Flask, send_from_directory, request, jsonify, abort
except Exception as e:
    raise RuntimeError("Flask is required to run the web server: %s" % e)

# requests is optional for the monitor; health monitor will disable if not present
try:
    import requests
    _REQUESTS_AVAILABLE = True
except Exception:
    requests = None
    _REQUESTS_AVAILABLE = False

ap = argparse.ArgumentParser(description="StaSh + Flask launcher (Flask foreground, StaSh background) with TLS and health-stop.")
ap.add_argument("--no-cfgfile", action="store_true")
ap.add_argument("--no-rcfile", action="store_true")
ap.add_argument("--no-historyfile", action="store_true")
ap.add_argument("--log-level", choices=["DEBUG","INFO","WARN","ERROR","CRITICAL"], default="INFO")
ap.add_argument("--log-file")
ap.add_argument("--debug-switch", default="")
ap.add_argument("-c","--command", default=None, help="single StaSh command to run then exit")
ap.add_argument("--flask-host", default="0.0.0.0")
ap.add_argument("--flask-port", type=int, default=int(os.environ.get("PORT",3000)))
ap.add_argument("--domain", default="cratejuice.guru", help="expected Host header")
ap.add_argument("--enforce-host", action="store_true", help="reject requests with wrong Host header")
ap.add_argument("--cert", default="./certs/fullchain.pem", help="TLS cert (PEM)")
ap.add_argument("--key", default="./certs/privkey.pem", help="TLS key (PEM)")
ap.add_argument("--health-interval", type=float, default=30.0, help="seconds between health checks")
ap.add_argument("--health-failures", type=int, default=3, help="consecutive failures before action")
ap.add_argument("--on-failure", choices=["stop","restart","webhook"], default="stop", help="action after health failures")
ap.add_argument("--restart-cmd", help="shell command to run on 'restart' action (e.g. 'systemctl restart cratejuice')")
ap.add_argument("--webhook-url", help="URL to POST to on 'webhook' action")
ap.add_argument("--pythonista", action="store_true", help="pythonista-friendly defaults")
ap.add_argument("--open-browser", action="store_true", help="open browser (skipped on Pythonista)")
ap.add_argument("args", nargs="*", help="ignored")
s = ap.parse_args()

# Logging
log_level = getattr(logging, ns.log_level, logging.INFO)
logging.basicConfig(filename=ns.log_file, level=log_level, format="%(asctime)s %(levelname)s %(message)s")

# Optional best-effort reloads for stash internals
module_names = [
    "stash",
    "system.shcommon","system.shstreams","system.shscreens","system.shui",
    "system.shui.base","system.shio","system.shiowrapper","system.shparsers",
    "system.shruntime","system.shthreads","system.shuseractionproxy","system.shhistory",
]
for name in module_names:
    full = name if name == "stash" or name.startswith("stash.") else "stash." + name
    try:
        if full in sys.modules:
            importlib.reload(sys.modules[full])
        else:
            importlib.import_module(full)
    except Exception:
        logging.debug("Could not reload/import %s", full)

# Parse stash debug switches into values list
debug_flags = []
if ns.debug_switch:
    if ns.debug_switch.strip().lower() == "all":
        for key in dir(stash):
            if key.startswith("_DEBUG_"):
                v = getattr(stash, key, None)
                if v is not None:
                    debug_flags.append(v)
    else:
        for ds in ns.debug_switch.split(","):
            ds = ds.strip()
            if ds:
                v = getattr(stash, f"_DEBUG_{ds.upper()}", None)
                if v is not None:
                    debug_flags.append(v)

ctp = False if ns.command else None
_stash = stash.StaSh(debug=debug_flags, log_setting={"level": ns.log_level, "file": ns.log_file}, no_cfgfile=ns.no_cfgfile, no_rcfile=ns.no_rcfile, no_historyfile=ns.no_historyfile, command=ctp)

# Flask app
script_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
static_dir = os.path.join(script_dir, "public")
app = Flask(__name__, static_folder=static_dir, static_url_path="")

@app.before_request
def enforce_host_header():
    if ns.enforce_host:
        host = request.host.split(":")[0] if request.host else ""
        if host.lower() != ns.domain.lower():
            logging.warning("Rejected request with host=%s (expected %s)", host, ns.domain)
            abort(400, description="Invalid Host header")

@app.route("/")
def serve_index():
    return send_from_directory(static_dir, "index.html")

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(static_dir, path)

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/_shutdown", methods=["POST"])
def _shutdown():
    if request.remote_addr not in ("127.0.0.1","localhost","::1"):
        return "Forbidden", 403
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        return "no shutdown function", 500
    func()
    return "shutting down", 200

# Health monitor
def is_port_open(host, port, timeout=1.0):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False


def health_monitor(host, port, interval, allowed_failures):
    use_ssl = os.path.exists(ns.cert) and os.path.exists(ns.key)
    scheme = "https" if use_ssl else "http"
    # use loopback to avoid firewall/NAT hairpin
    url = f"{scheme}://127.0.0.1:{port}/health"
    consecutive = 0
    verify = False if use_ssl else True
    logging.info("Health monitor checking %s every %.1fs; threshold=%d", url, interval, allowed_failures)
    while True:
        try:
            if not _REQUESTS_AVAILABLE:
                raise RuntimeError("requests not available")
            resp = requests.get(url, timeout=5, verify=verify, headers={"Host": ns.domain})
            if resp.status_code == 200:
                consecutive = 0
            else:
                consecutive += 1
                logging.warning("Health returned %s (consec %d)", resp.status_code, consecutive)
        except Exception as e:
            consecutive += 1
            logging.warning("Health error: %s (consec %d)", e, consecutive)
        if consecutive >= allowed_failures:
            logging.error("Health check failed %d times; performing on-failure=%s", consecutive, ns.on_failure)
            try:
                if ns.on_failure == "stop":
                    if _REQUESTS_AVAILABLE:
                        requests.post(f"http://127.0.0.1:{port}/_shutdown", timeout=3)
                    else:
                        os._exit(1)
                elif ns.on_failure == "restart" and ns.restart_cmd:
                    subprocess.Popen(ns.restart_cmd, shell=True)
                elif ns.on_failure == "webhook" and ns.webhook_url and _REQUESTS_AVAILABLE:
                    requests.post(ns.webhook_url, json={"status":"unhealthy","domain":ns.domain}, timeout=5)
            except Exception:
                logging.exception("Failed to perform on-failure action")
            break
        time.sleep(interval)

# Launch StaSh in background thread
def _launch_stash():
    try:
        _stash.launch(ctp)
    except Exception:
        logging.exception("StaSh launch failed")

stash_thread = threading.Thread(target=_launch_stash, daemon=True)
stash_thread.start()

# If -c provided, run single command and exit
if ns.command:
    try:
        _stash(ns.command, add_to_history=False, persistent_level=0)
    except Exception:
        logging.exception("Error running command")
    try:
        if _REQUESTS_AVAILABLE:
            requests.post(f"http://127.0.0.1:{ns.flask_port}/_shutdown", timeout=1)
    except Exception:
        pass
    sys.exit(0)

# Start health monitor thread if requests available
if _REQUESTS_AVAILABLE:
    monitor_thread = threading.Thread(target=health_monitor, args=(ns.domain, ns.flask_port, ns.health_interval, ns.health_failures), daemon=True)
    monitor_thread.start()
else:
    logging.info("requests not available: health monitor disabled")

# TLS context
use_ssl = os.path.exists(ns.cert) and os.path.exists(ns.key)
ssl_context = (ns.cert, ns.key) if use_ssl else None
if use_ssl:
    logging.info("Starting Flask with TLS on %s:%d (domain %s)", ns.flask_host, ns.flask_port, ns.domain)
else:
    logging.info("Starting Flask without TLS on %s:%d (domain %s)", ns.flask_host, ns.flask_port, ns.domain)

# Pythonista consideration
is_pythonista = ns.pythonista or os.environ.get("PYTHONISTA") or sys.platform.startswith("ios") or ("Pythonista" in (sys.executable or ""))
flask_debug = False
app.run(host=ns.flask_host, port=ns.flask_port, debug=flask_debug, use_reloader=False, threaded=True, ssl_context=ssl_context)