#!/usr/bin/env bash
# Baixa as 11 gravações reais de clarinete para samples/clarinet/ (tonejs-instruments, CC BY 3.0).
set -e
BASE="https://cdn.jsdelivr.net/gh/nbrosowsky/tonejs-instruments@master/samples/clarinet"
DEST="$(cd "$(dirname "$0")/.." && pwd)/samples/clarinet"
mkdir -p "$DEST"
for f in D3 F3 As3 D4 F4 As4 D5 F5 As5 D6 Fs6; do
  curl -fsSL "$BASE/$f.mp3" -o "$DEST/$f.mp3" && echo "ok   $f.mp3"
done
echo "Concluído."
