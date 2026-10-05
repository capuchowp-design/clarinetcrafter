#!/usr/bin/env python3
"""Baixa as 11 gravações reais de clarinete para samples/clarinet/ (uso offline e hospedagem própria).
Fonte: tonejs-instruments (N. P. Brosowsky), samples sob licença CC BY 3.0.
Uso:  python3 tools/baixar-amostras.py
"""
import os, sys, urllib.request

BASE = "https://cdn.jsdelivr.net/gh/nbrosowsky/tonejs-instruments@master/samples/clarinet/"
FILES = ["D3", "F3", "As3", "D4", "F4", "As4", "D5", "F5", "As5", "D6", "Fs6"]
dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "samples", "clarinet")
os.makedirs(dest, exist_ok=True)

falhas = 0
for f in FILES:
    ok = False
    for ext in (".mp3", ".ogg"):
        try:
            with urllib.request.urlopen(BASE + f + ext, timeout=30) as r:
                data = r.read()
            open(os.path.join(dest, f + ext), "wb").write(data)
            print("ok  ", f + ext, len(data), "bytes")
            ok = True
            break
        except Exception as e:
            err = e
    if not ok:
        falhas += 1
        print("ERRO", f, err)
print("\nConcluído." if not falhas else "\n%d arquivo(s) falharam." % falhas)
sys.exit(1 if falhas else 0)
