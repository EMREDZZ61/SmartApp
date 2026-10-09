#Smart App: hoofdmenu dat alle onderdelen samenbrengt.
from weerstation import weerstation, Fahrenheit, weerrapport
from controller import smart_app_controller
from weer_api import haal_huidig_weer


def toon_huidig_weer():
    weer = haal_huidig_weer()
    if weer is None:
        return

    t = weer["temperatuur"]
    w = weer["windsnelheid"]
    v = weer["vochtigheid"]
    print("\nHuidig weer in Utrecht:")
    print(f"Temperatuur: {t:.1f}C ({Fahrenheit(t):.1f}F)")
    print(f"Windsnelheid: {w:.1f} m/s")
    print(f"Luchtvochtigheid: {v}%")
    print(weerrapport(t, w, v))


def hoofdmenu():
    print("Welkom bij de Smart App!")

    while True:
        print()
        print("=== HOOFDMENU ===")
        print("1. Weerstation (weer van 7 dagen invoeren)")
        print("2. Smart App Controller (actuatoren)")
        print("3. Huidig weer in Utrecht (live)")
        print("4. Stoppen")
        keuze = input("Maak een keuze (1-4): ").strip()

        if keuze == "1":
            weerstation()
        elif keuze == "2":
            smart_app_controller()
        elif keuze == "3":
            toon_huidig_weer()
        elif keuze == "4":
            print("Tot ziens!")
            break
        else:
            print("Ongeldige keuze, kies een getal van 1 t/m 4.")


if __name__ == "__main__":
    try:
        hoofdmenu()
    except (KeyboardInterrupt, EOFError):
        print("\nProgramma afgesloten.")