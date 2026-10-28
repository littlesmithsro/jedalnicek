#!/usr/bin/env python3
"""Generuje oba identické offline súbory zo spoločnej šablóny."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def build():
    content = (ROOT / 'template.html').read_text()
    for name in ('index.html', 'jedalnicek.html'):
        (ROOT / name).write_text(content)
    print('Vygenerované: index.html, jedalnicek.html')

if __name__ == '__main__':
    build()
