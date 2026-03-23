#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from functools import partial
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".avif", ".heic", ".heif"}
ROOT = Path(__file__).resolve().parent
PHOTOS_DIR = ROOT / "photos"
MANIFEST_PATH = PHOTOS_DIR / "manifest.local.json"
TAGS_LOCAL_PATH = ROOT / "tags.local.json"
TAGS_TEMPLATE_PATH = ROOT / "tags.template.json"


def scan_photos() -> list[str]:
    if not PHOTOS_DIR.exists():
        return []

    files: list[str] = []
    for path in sorted(PHOTOS_DIR.iterdir(), key=lambda p: p.name.lower()):
        if not path.is_file():
            continue
        if path.name.startswith("manifest."):
            continue
        if path.suffix.lower() not in IMAGE_EXTS:
            continue
        files.append(path.name)
    return files


def write_manifest() -> dict[str, list[str]]:
    PHOTOS_DIR.mkdir(parents=True, exist_ok=True)
    payload = {"files": scan_photos()}
    MANIFEST_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload


def ensure_tags_file() -> dict:
    if TAGS_LOCAL_PATH.exists():
        try:
            return json.loads(TAGS_LOCAL_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass

    if TAGS_TEMPLATE_PATH.exists():
        try:
            payload = json.loads(TAGS_TEMPLATE_PATH.read_text(encoding="utf-8"))
            TAGS_LOCAL_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
            return payload
        except json.JSONDecodeError:
            pass

    payload: dict = {}
    TAGS_LOCAL_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload


def write_tags(payload: dict) -> dict:
    if not isinstance(payload, dict):
        payload = {}
    TAGS_LOCAL_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload


class GalleryHandler(SimpleHTTPRequestHandler):
    def _send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_POST(self) -> None:
        if self.path.rstrip("/") == "/__refresh_manifest":
            payload = write_manifest()
            self._send_json(HTTPStatus.OK, {"ok": True, "files": payload["files"], "manifest": "photos/manifest.local.json"})
            return
        if self.path.rstrip("/") == "/__save_tags":
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length) if length else b"{}"
            try:
                payload = json.loads(raw.decode("utf-8"))
            except json.JSONDecodeError:
                self._send_json(HTTPStatus.BAD_REQUEST, {"ok": False, "error": "Invalid JSON"})
                return
            saved = write_tags(payload)
            self._send_json(HTTPStatus.OK, {"ok": True, "count": len(saved), "tags": "tags.local.json"})
            return
        self._send_json(HTTPStatus.NOT_FOUND, {"ok": False, "error": "Not found"})

    def do_GET(self) -> None:
        if self.path.rstrip("/") == "/__manifest_status":
            payload = write_manifest()
            self._send_json(HTTPStatus.OK, {"ok": True, "files": payload["files"], "manifest": "photos/manifest.local.json"})
            return
        if self.path.rstrip("/") == "/__tags_status":
            payload = ensure_tags_file()
            self._send_json(HTTPStatus.OK, {"ok": True, "count": len(payload), "tags": "tags.local.json"})
            return
        return super().do_GET()


def main() -> None:
    parser = argparse.ArgumentParser(description="Family Gallery local server")
    parser.add_argument("--port", type=int, default=4173)
    args = parser.parse_args()

    write_manifest()
    ensure_tags_file()
    handler = partial(GalleryHandler, directory=str(ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    url = f"http://127.0.0.1:{args.port}/gallery.html"
    print(f"Serving Family Gallery at {url}")
    print(f"Manifest path: {MANIFEST_PATH}")
    print("Press Ctrl+C to stop the server.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
