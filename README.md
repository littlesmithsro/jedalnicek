# Jedálniček

Jednosúborová offline app (žiadne CDN, žiadny server).

- `index.html` – celá aplikácia: hore editovateľné celkové kcal a makrá (auto-prepočet podľa noriem), 4 jedlá denne (každý deň rovnaké), live gramáže, dole nákupný zoznam na týždeň
- `jedalnicek.html` – identický súbor na stiahnutie

- `template.html` – zdrojová šablóna; úpravy rob tu
- `build.py` – `python3 build.py` vygeneruje oba identické HTML súbory
- Nastavenia, gramáže, nutričné hodnoty a odškrtnutý nákup sa automaticky ukladajú do localStorage v danom prehliadači. Export JSON obsahuje aj tieto údaje; import JSON zatiaľ nie je implementovaný.
- Reset obnoví aj pôvodné nutričné hodnoty. Nastavenie v zdieľanom odkaze má prednosť pred uloženými gramážami/cieľmi.
- Mäso: kuracie sa váži po tepelnej úprave; hovädzie surové. Hovädzie má iba orientačné údaje pre 20 % tuku, nie overenú etiketu konkrétneho výrobku.

Web: https://littlesmithsro.github.io/jedalnicek/
