#!/usr/bin/env bash
# Baixa as 11 gravações reais de clarinete (tonejs-instruments, CC-BY 3.0) para samples/clarinet/
set -e
cd "$(dirname "$0")"
mkdir -p samples/clarinet
BASE="https://raw.githubusercontent.com/nbrosowsky/tonejs-instruments/master/samples/clarinet"
for n in D3 F3 As3 D4 F4 As4 D5 F5 As5 D6 Fs6; do
  echo "baixando $n.mp3"
  curl -fL --retry 3 -o "samples/clarinet/$n.mp3" "$BASE/$n.mp3"
done
echo "Pronto: $(ls samples/clarinet | wc -l) arquivos em samples/clarinet"
