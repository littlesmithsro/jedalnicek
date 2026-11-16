# Jedálniček

Jednosúborová offline app (žiadne CDN, žiadny server).

- `index.html` – celá aplikácia: hore editovateľné ciele (kcal a makrá s automatickým prepočtom podľa noriem), 4 jedlá denne (každý deň rovnaké), live gramáže, karta PROGRES s históriou váh, dole nákupný zoznam na týždeň
- `jedalnicek.html` – identický súbor na stiahnutie

- `template.html` – zdrojová šablóna; úpravy rob tu
- `build.py` – `python3 build.py` vygeneruje oba identické HTML súbory; overuje, že v každom food bloku nájde riadky `fval` a `fm`
- Nastavenia, gramáže, nutričné hodnoty, odškrtnutý nákup a história váh sa automaticky ukladajú do localStorage v danom prehliadači (kľúče `jedalnicek.settings.v1` a `jedalnicek.progress.v1`).
- Export JSON je verzia 3 a obsahuje aj históriu váh; Import JSON ju vie vrátiť späť. Reset obnoví plán, ciele a výživové hodnoty, históriu váh nemení.
- Zdieľaný odkaz obsahuje gramáže, ciele, dni, hmotnosť a výdaj; nastavenie v odkaze má prednosť pred uloženým stavom.

## Progres

- Karta PROGRES: zápis hmotnosti s dátumom (raz týždenne stačí), trend z lineárnej regresie za posledných 21 dní, graf v inline SVG.
- Odporúčanie mení kalórie najviac o ±200 kcal na krok, cieľový úbytok 0,7 % hmotnosti za týždeň, podlaha 1800 kcal. Pri plaťe (menej ako 0,2 kg/týždeň) appka kalórie neznižuje.
- Prispôsobenie porcií sa počíta z pôvodných gramáží (`data-base`), preto rovnaký cieľ vždy dá rovnaký plán bez ohľadu na poradie predchádzajúcich zmien. Menia sa sacharidy a tuky; bielkoviny a zelenina zostávajú.
- Tlačidlo „Text reportu" vygeneruje krátky týždenný súhrn na skopírovanie.

## Váženie surovín

Mäso, zemiaky a zelenina sa vážia surové; vločky suché; vajcia bez škrupiny. Kuracie prsia: orientačne 120 kcal, 22,5 g P a 2,6 g F/100 g, základná porcia 300 g surového mäsa (zdroj: https://chicken.foodnutrify.com/chicken/breast-skinless-boneless). Hovädzie má iba orientačné údaje pre 20 % tuku, nie overenú etiketu konkrétneho výrobku. Staré uložené porcie kuracieho a odkazy sa približne prepočítajú podľa bielkovín; nejde o garantovaný výťažok varenia.

Web: https://littlesmithsro.github.io/jedalnicek/
