# WeerWijs (SmartApp)

*Slim weer. Slim huis.*

Smart App van Emre Danismaz (1910119), HBO-ICT.

SmartApp bestaat uit een Weerstation dat 7 dagen weersdata verwerkt en rapporten maakt, een Smart Controller die txt-daggegevens leest, actuatoren berekent (CV, ventilatie, bewatering) en via een menu dagen toont, berekent of waarden overschrijft, en het live weer van Utrecht via de Open-Meteo API.

## Starten

Run `main.py` en kies een optie in het hoofdmenu:

1. Weerstation (weer van 7 dagen invoeren)
2. Smart App Controller (actuatoren berekenen en overschrijven)
3. Huidig weer in Utrecht (internet nodig)
4. Stoppen

## Bestanden

| Bestand | Wat het doet |
|---|---|
| `main.py` | Hoofdmenu |
| `weerstation.py` | Sprint 1: weerrapport per dag |
| `controller.py` | Sprint 2: actuatoren berekenen uit `data/invoer.txt` en opslaan in `data/uitvoer.txt` |
| `weer_api.py` | Sprint 3: live weer via Open-Meteo |
| `data/` | Invoer- en uitvoerbestand |
