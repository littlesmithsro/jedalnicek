# Overenie úprav

Overené priamo v prehliadači nad lokálnym index.html:

- Zmena gramáže, kcal cieľa, počtu dní, tukov hovädzieho a odškrtnutie nákupu sa zachovali po novom načítaní.
- Uložená nutričná hodnota sa obnovila aj do dát všetkých zodpovedajúcich potravín, nielen do políčka.
- Reset obnovil cieľ, pôvodné gramáže, nutričné hodnoty aj nákup.
- Slider zmenil číslo i denný súčet; prispôsobenie porcií zmenilo gramáže; nesúlad slider/číselné pole: 0.
- Šírky 375 a 320 px: bez vodorovného pretečenia stránky.
- Poškodené JSON úložisko nezastavilo aplikáciu a zobrazilo upozornenie.
- Zablokovaný zápis do úložiska nezastavil prepočty a zobrazil upozornenie.
- Zdieľaný odkaz prepísal uložené gramáže, ciele a dni. Opravené načítanie aj pri zmene samotného fragmentu na už otvorenej stránke.
- `python3 build.py` a `git diff --check`: úspešné; index.html, jedalnicek.html a template.html sú identické.

Nutričné hodnoty neboli overované proti etikete výrobku. Rozpor 15/20 % bol odstránený z názvu; hodnoty zostali orientačné a plán bez zmeny porcií. Referenčný deň: 2315,02 kcal, 194,19 g P, 214,25 g C, 77,9 g F.
