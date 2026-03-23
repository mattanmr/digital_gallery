#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")"
PORT=4173
URL="http://127.0.0.1:${PORT}/gallery.html"

if ! command -v python3 >/dev/null 2>&1; then
  osascript -e 'display alert "Python 3 not found" message "Install Python 3 to run the gallery server." as critical'
  exit 1
fi

echo "Starting Family Gallery server on ${URL}"
echo "Keep this window open while using the gallery."
echo "Press Ctrl+C to stop the server."

(sleep 1; open "$URL") &
exec python3 gallery_server.py --port "$PORT"
