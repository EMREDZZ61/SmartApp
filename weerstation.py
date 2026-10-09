#Sprint 1: Weerstation.


def Fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - luchtvochtigheid / 100 * windsnelheid


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif gevoel < 10:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"


def vraag_waarde(vraag, als_geheel=False, min_waarde=None, max_waarde=None):
    while True:
        invoer = input(vraag).strip()
        if invoer == "":
            return None

        try:
            if als_geheel:
                waarde = int(invoer)
            else:
                waarde = float(invoer)
        except ValueError:
            print("Ongeldige invoer, voer een getal in.")
            continue

        if waarde != waarde or waarde in (float("inf"), float("-inf")):
            print("Ongeldige invoer, voer een gewoon getal in.")
            continue
        if min_waarde is not None and waarde < min_waarde:
            print(f"De waarde moet minimaal {min_waarde} zijn.")
            continue
        if max_waarde is not None and waarde > max_waarde:
            print(f"De waarde mag maximaal {max_waarde} zijn.")
            continue

        return waarde


def weerstation():
    totaal = 0

    for dag in range(1, 8):
        temperatuur = vraag_waarde(f"Wat is op dag {dag} de temperatuur[C]: ")
        if temperatuur is None:
            print("bye")
            return

        windsnelheid = vraag_waarde(
            f"Wat is op dag {dag} de windsnelheid[m/s]: ", min_waarde=0
        )
        if windsnelheid is None:
            print("bye")
            return

        luchtvochtigheid = vraag_waarde(
            f"Wat is op dag {dag} de vochtigheid[%]: ",
            als_geheel=True, min_waarde=0, max_waarde=100
        )
        if luchtvochtigheid is None:
            print("bye")
            return

        totaal += temperatuur

        print(f"Het is {temperatuur:.1f}C ({Fahrenheit(temperatuur):.1f}F)")
        print(weerrapport(temperatuur, windsnelheid, luchtvochtigheid))
        print(f"Gem. temp tot nu toe is {totaal / dag:.1f}")
        print("=" * 38)


# Deze regel zorgt dat het weerstation niet start als je dit bestand importeert
if __name__ == "__main__":
    weerstation()