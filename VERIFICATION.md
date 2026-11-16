# Overenie úprav

## Progres v2 (2026-11-16)

Overené v reálnom prehliadači (Chromium, 375 × 812 a 320 × 700, stránka cez `http://127.0.0.1:8811`) po `python3 build.py`.

### Prispôsobenie porcií

- `adapt()` škáluje od `data-base` potravín, nie od aktuálnych gramáží. Poradie zmien už nemení výsledok.
- Postupný test cieľov v jednej relácii: 1800 kcal → 2000 kcal (+11 %), 3300 kcal → 3163 kcal (−4 %), 2300 kcal → 2286 kcal (−1 %).
- Idempotencia: cieľ 3300 kcal z čistého stavu a po predchádzajúcom 1800 kcal dal **identické gramáže** všetkých 20 potravín (`gramsIdentickeSČistým: true`).
- Predtým (chyba): 1800 → 3300 skončil na 2255 kcal (−32 %); už sa nevyskytuje.
- Zvyškový rozdiel po prispôsobení je zámerný: bielkoviny a zelenina sa nemenia, appka rozdiel vypisuje.

### Denný súčet a rozloženie

- Sticky lišta `#stickBar`: pri scrollovaní za kartu súčtu sa zobrazí (výška 29 px), ukazuje kcal + rozdiel + P/C/F, aktualizuje sa pri zmene gramáží. Pri scrolle na začiatok sa skryje (`aria-hidden="true"`).
- Karta cieľov je rozdelená na blok „Vstupy" (sivý) a „Cieľ (vypočíta sa, dá sa prepísať)" (modrastý).
- Dlhé vysvetľujúce texty sú v zatvorenom `<details>`; `#msg` zostal mimo `<details>`, takže hlášky sú viditeľné.

### Progres

- Karta PROGRES: zápis dátumu a hmotnosti, prepis pri rovnakom dátume, mazanie záznamu, zoznam posledných 10 meraní.
- Trend (lineárna regresia za 21 dní): váhy 110,0 kg (26. 10.), 108,6 kg (2. 11.), 107,4 kg (9. 11.) → **−1,30 kg/týždeň**, 3 merania / 14 dní.
- Odporúčanie: cieľový úbytok 0,7 % hmotnosti/týždeň, max. zmena ±200 kcal, podlaha 1800 kcal. Pri trende −1,2 kg/týždeň navrhlo +200 kcal (2300 → 2500); po aplikovaní denný súčet 2547 kcal (+2 %).
- Plaťo (|trend| < 0,2 kg/týždeň) kalórie neznižuje, len vypíše upozornenie a odporúčanie vypne.
- Po reloade sa obnovili: cieľ, hmotnosť (aj popisok v hlavičke), zoznam váh a trend.

### Export / import

- JSON verzie 3 obsahuje históriu váh. Export → reset → import obnovil cieľ 2500 kcal, denný súčet 2547 kcal aj 3 záznamy váh.
- Poškodený JSON: `importJson` vráti `false`, denný súčet zostal nezmenený, zobrazila sa hláška.
- Reset nemení históriu váh — obnoví iba plán, ciele a výživové hodnoty.

### Prístupnosť, šírky, tlač

- Chýbajúce `label`/`aria-label` pri vstupoch: **0** (80 vstupov v tabuľke hodnôt a 16 checkboxov nákupu dostalo `aria-label`).
- Ovládače nižšie ako 38 px na 375 px: **žiadne**.
- 320 px: `scrollWidth === 320`, bez vodorovného pretečenia, sticky lišta v jednom riadku.
- `@media print` je prítomné: skrýva lištu, tlačidlá a hlavičku, nákupný zoznam drží pokope.

### Build

- `build.py` už nepredpokladá pevné offsety `i+1`/`i+3`; hľadá `fval`/`fm` v okne 6 riadkov a pri nenájdení skončí s chybou.
- `python3 build.py` je idempotentný (rovnaký hash pri opakovanom behu), `index.html` a `jedalnicek.html` sú bit-identické.
- JavaScript prechádza `node --check` bez chýb; `window.__jedalnicek` exponuje 19 funkcií.

## Základná verzia

Overené priamo v prehliadači nad lokálnym index.html:

- Zmena gramáže, kcal cieľa, počtu dní, tukov hovädzieho a odškrtnutie nákupu sa zachovali po novom načítaní.
- Uložená nutričná hodnota sa obnovila aj do dát všetkých zodpovedajúcich potravín, nielen do políčka.
- Reset obnovil cieľ, pôvodné gramáže, nutričné hodnoty aj nákup.
- Slider zmenil číslo i denný súčet; prispôsobenie porcií zmenilo gramáže; nesúlad slider/číselné pole: 0.
- Šírky 375 a 320 px: bez vodorovného pretečenia stránky.
- Poškodené JSON úložisko nezastavilo aplikáciu a zobrazilo upozornenie.
- Zablokovaný zápis do úložiska nezastavil prepočty a zobrazilo upozornenie.
- Zdieľaný odkaz prepísal uložené gramáže, ciele a dni. Opravené načítanie aj pri zmene samotného fragmentu na už otvorenej stránke.
- `python3 build.py` a `git diff --check`: úspešné; index.html, jedalnicek.html a template.html sú identické.

Nutričné hodnoty neboli overované proti etikete výrobku. Rozpor 15/20 % bol odstránený z názvu; hodnoty zostali orientačné a plán bez zmeny porcií. Referenčný deň: 2312,02 kcal, 193,49 g P, 214,25 g C, 77,78 g F, 41,37 g vlákniny.
