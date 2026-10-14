#!/usr/bin/env python3
"""Monta a pasta www/ (o app que vai dentro do APK) a partir dos arquivos do repositório.

- Copia index.html, manifest.json, privacy.html e os ícones (NÃO copia sw.js: no APK não precisa).
- Troca o VexFlow da internet pela cópia local (node_modules/vexflow) -> a partitura funciona offline.
- Copia as gravações do clarinete (pasta samples/, baixada pelo workflow) e tira o endereço da internet das gravações.
"""
import glob, os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WWW = os.path.join(ROOT, "www")
VENDOR = os.path.join(WWW, "vendor")

if os.path.isdir(WWW):
    shutil.rmtree(WWW)
os.makedirs(VENDOR)

for name in ["index.html", "manifest.json", "privacy.html"]:
    src = os.path.join(ROOT, name)
    if os.path.exists(src):
        shutil.copy(src, WWW)
for f in glob.glob(os.path.join(ROOT, "*.png")):
    shutil.copy(f, WWW)

def die(msg):
    print("ERRO:", msg)
    sys.exit(1)

index_path = os.path.join(WWW, "index.html")
html = open(index_path, encoding="utf-8").read()

# 1) VexFlow local
vf_src = os.path.join(ROOT, "node_modules", "vexflow", "build", "cjs", "vexflow.js")
vf_tag = '<script src="https://cdn.jsdelivr.net/npm/vexflow@4.2.5/build/cjs/vexflow.js"></script>'
if not os.path.exists(vf_src):
    die("VexFlow não encontrado em node_modules (rode npm install).")
if vf_tag not in html:
    die("não achei a linha do VexFlow no index.html")
shutil.copy(vf_src, os.path.join(VENDOR, "vexflow.js"))
html = html.replace(vf_tag, '<script src="vendor/vexflow.js"></script>')
print("VexFlow: local")

# 2) gravações do clarinete
need = ["D3", "F3", "As3", "D4", "F4", "As4", "D5", "F5", "As5", "D6", "Fs6"]
sdir = os.path.join(ROOT, "samples", "clarinet")
missing = [n for n in need if not os.path.exists(os.path.join(sdir, n + ".mp3"))]
if missing:
    die("faltam gravações em samples/clarinet: " + ", ".join(missing))
shutil.copytree(os.path.join(ROOT, "samples"), os.path.join(WWW, "samples"))
cdn = ", 'https://cdn.jsdelivr.net/gh/nbrosowsky/tonejs-instruments@master/samples/clarinet/'"
if cdn not in html:
    die("não achei o endereço da internet das gravações no index.html")
html = html.replace(cdn, "")
print("Gravações: locais (%d arquivos)" % len(need))

open(index_path, "w", encoding="utf-8").write(html)
print("www pronto:", sorted(os.listdir(WWW)))
