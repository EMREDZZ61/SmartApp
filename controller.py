#Sprint 2: Smart App Controller."""
import os

import os

MAP = os.path.dirname(os.path.abspath(__file__))
INVOER_BESTAND = os.path.join(MAP, "data", "invoer.txt")
UITVOER_BESTAND = os.path.join(MAP, "data", "uitvoer.txt")


def lees_dagen(inputFile):
    with open(inputFile, "r", encoding="utf-8") as f:
        regels = [regel.strip() for regel in f.readlines()]
    regels = [regel for regel in regels if regel != ""]
    return regels[1:]


def aantal_dagen(inputFile):
    return len(lees_dagen(inputFile))


def auto_bereken(inputFile, outputFile):
    regels = lees_dagen(inputFile)
    resultaat = []

    for nummer, regel in enumerate(regels, start=2):
        delen = regel.split()
        if len(delen) != 5:
            raise ValueError(f"Regel {nummer} heeft niet 5 velden: '{regel}'")
        try:
            datum = delen[0]
            personen = int(float(delen[1]))
            setpoint = float(delen[2])
            buiten = float(delen[3])
            neerslag = float(delen[4])
        except ValueError:
            raise ValueError(f"Regel {nummer} bevat een ongeldig getal: '{regel}'")

        verschil = setpoint - buiten
        if verschil >= 20:
            cv = 100
        elif verschil >= 10:
            cv = 50
        else:
            cv = 0

        ventilatie = min(personen + 1, 4)
        bewatering = neerslag < 3

        resultaat.append(f"{datum};{cv};{ventilatie};{bewatering}")

    with open(outputFile, "w", encoding="utf-8") as f:
        for regel in resultaat:
            f.write(regel + "\n")


def overwrite_settings(outputFile):
    #Geeft 0 (gelukt), -1 (datum niet gevonden) of -3 (ongeldig systeem/waarde) terug.
    datum = input("Welke datum wil je aanpassen (dd-mm-jjjj)? ").strip()

    try:
        with open(outputFile, "r", encoding="utf-8") as f:
            regels = [regel.strip() for regel in f.readlines() if regel.strip() != ""]
    except FileNotFoundError:
        return -1

    index = None
    for i, regel in enumerate(regels):
        if regel.split(";")[0] == datum:
            index = i
            break
    if index is None:
        return -1

    systeem = input("Welk systeem (1: CV ketel, 2: ventilatie, 3: bewatering)? ").strip()
    if systeem not in ("1", "2", "3"):
        return -3

    waarde = input("Welke nieuwe waarde? ").strip()
    maximaal = {"1": 100, "2": 4, "3": 1}[systeem]
    try:
        getal = int(waarde)
    except ValueError:
        return -3
    if not 0 <= getal <= maximaal:
        return -3

    delen = regels[index].split(";")
    if systeem == "3":
        delen[3] = "True" if getal == 1 else "False"
    else:
        delen[int(systeem)] = str(getal)
    regels[index] = ";".join(delen)

    with open(outputFile, "w", encoding="utf-8") as f:
        for regel in regels:
            f.write(regel + "\n")
    return 0


def smart_app_controller():
    print("\nSmart App Controller")
    print("Berekent actuatoren (CV ketel, ventilatie, bewatering) uit weerdata.")
    print("Tip: kies eerst optie 2 voordat je optie 3 gebruikt.")

    while True:
        print()
        print("--- Controller ---")
        print("1. Hoeveel dagen zijn er aanwezig?")
        print("2. Automatisch alle actuatoren berekenen en opslaan")
        print("3. Een berekende waarde overschrijven")
        print("4. Terug naar hoofdmenu")
        keuze = input("Maak een keuze (1-4): ").strip()

        if keuze == "1":
            try:
                print(f"Er zijn {aantal_dagen(INVOER_BESTAND)} dagen in het invoerbestand.")
            except FileNotFoundError:
                print(f"Fout: invoerbestand niet gevonden ({INVOER_BESTAND}).")

        elif keuze == "2":
            try:
                auto_bereken(INVOER_BESTAND, UITVOER_BESTAND)
                print("Gelukt! De waarden zijn naar het uitvoerbestand geschreven.")
            except FileNotFoundError:
                print(f"Fout: invoerbestand niet gevonden ({INVOER_BESTAND}).")
            except ValueError as fout:
                print(f"Fout in invoerbestand: {fout}")

        elif keuze == "3":
            if not os.path.exists(UITVOER_BESTAND):
                print("Fout: er is nog geen uitvoerbestand. Kies eerst optie 2.")
                continue
            resultaat = overwrite_settings(UITVOER_BESTAND)
            if resultaat == 0:
                print("Gelukt! De waarde is overschreven in het uitvoerbestand.")
            elif resultaat == -1:
                print("Fout: datum niet gevonden.")
            else:
                print("Fout: ongeldig systeem gekozen of ongeldige waarde ingevoerd.")

        elif keuze == "4":
            break

        else:
            print("Ongeldige keuze, kies een getal van 1 t/m 4.")


if __name__ == "__main__":
    smart_app_controller()