#!/usr/bin/env python3
"""Generuje offline HTML a predpočíta hodnoty aj bez JavaScriptu."""
from pathlib import Path
import re
from collections import defaultdict

ROOT = Path(__file__).resolve().parent
KEYS = ('kcal', 'p', 'c', 'f', 'fib')

def rounded(value):
    return str(int(value + 0.5))

def build():
    content = (ROOT / 'template.html').read_text()
    meals: dict[str, dict[str, float]] = defaultdict(lambda: dict.fromkeys(KEYS, 0.0))
    shopping = defaultdict(float)
    current = None
    lines = content.splitlines()
    for i, line in enumerate(lines):
        match = re.search(r'<article class="card meal" data-mk="([^"]+)"', line)
        if match:
            current = match[1]
        if '<div class="food" ' not in line:
            continue
        assert current is not None
        data = dict(re.findall(r'data-([\w-]+)="([^"]*)"', line))
        grams = float(data['base'])
        values = {k: float(data[k]) * grams / 100 for k in KEYS}
        for k in KEYS:
            meals[current][k] += values[k]
        shopping[data['fk']] += grams
        lines[i+1] = re.sub(r'(<span class="fval">).*?(</span>)', lambda m: m[1]+rounded(grams)+' g'+m[2], lines[i+1])
        lines[i+3] = '        <div class="fm">'+rounded(values['kcal'])+' kcal · '+ ' · '.join(f'{values[k]:.1f} g {label}' for k,label in [('p','P'),('c','C'),('f','F')])+'</div>'
    content = '\n'.join(lines)+'\n'
    totals = {k: sum(m[k] for m in meals.values()) for k in KEYS}
    for meal, values in meals.items():
        text = '<b>'+rounded(values['kcal'])+' kcal</b> · '+' · '.join(rounded(values[k])+' g '+label for k,label in [('p','P'),('c','C'),('f','F'),('fib','vlákniny')])
        content = re.sub(r'(<div class="mtot" data-tot="'+meal+r'">).*?(</div>)', lambda m: m[1]+text+m[2], content)
    for k in KEYS:
        for attr, value in [('out', totals[k]), ('wk', totals[k]*7)]:
            content = re.sub(r'(data-'+attr+'="'+k+r'">)[\d.]+', lambda m: m[1]+rounded(value), content)
    def shop_row(match):
        row = match[0]
        key = re.search(r'data-fk="([^"]+)"', row)
        assert key is not None
        fk = key[1]
        grams = shopping[fk]
        week = grams*7
        qty = f'{week/1000:.2f}'.replace('.', ',')+' kg' if week>=1000 else rounded(week)+' g'
        row = re.sub(r'(<td class="dose">).*?(</td>)', lambda m: m[1]+rounded(grams)+' g / deň'+m[2], row)
        return re.sub(r'(<td class="qty sweek">).*?(</td>)', lambda m: m[1]+qty+m[2], row)
    content = re.sub(r'<tr class="shop-row"[^\n]+</tr>', shop_row, content)
    for name in ('index.html', 'jedalnicek.html'):
        (ROOT / name).write_text(content)
    print('Denný súčet:', {k: round(v,2) for k,v in totals.items()})
    print('Vygenerované: index.html, jedalnicek.html')

if __name__ == '__main__':
    build()
