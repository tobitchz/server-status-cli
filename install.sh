#!/usr/bin/env bash

set -e

echo "instalando servercheck..."

URL="https://raw.githubusercontent.com/tobitchz/server-status-cli/main/server_status_cli.py"
DEST="/usr/local/bin/servercheck"

sudo curl -L "$URL" -o "$DEST"
sudo chmod +x "$DEST"

echo "listo"
echo "usa: servercheck"
