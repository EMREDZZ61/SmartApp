def Fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - luchtvochtigheid / 100 * windsnelheid


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Heel koud en storm! Verwarming helemaal aan!"
    elif gevoel < 0:
        return "Behoorlijk koud! Verwarming beneden aan!"
    elif gevoel < 10 and windsnelheid > 12:
        return "Best koud en veel wind! Verwarming aan!"
    elif gevoel < 10:
        return "Een beetje koud! Elektrische kachel aan!"
    elif gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"


def weerstation():
    totaal = 0

    for dag in range(1, 8):
        try:
            temperatuur = input(f"Temperatuur dag {dag}: ")
            if temperatuur == "":
                print("bye")
                return

            windsnelheid = input(f"Windsnelheid dag {dag}: ")
            if windsnelheid == "":
                print("bye")
                return

            luchtvochtigheid = input(f"Luchtvochtigheid dag {dag}: ")
            if luchtvochtigheid == "":
                print("bye")
                return

            temperatuur = float(temperatuur)
            windsnelheid = float(windsnelheid)
            luchtvochtigheid = int(luchtvochtigheid)

            if not 0 <= luchtvochtigheid <= 100:
                print("Vochtigheid moet tussen 0 en 100 liggen.")
                return

        except ValueError:
            print("Gebruik alleen getallen.")
            return

        totaal += temperatuur


        print(f"\n{temperatuur}C ({Fahrenheit(temperatuur)}F)")
        print(weerrapport(temperatuur, windsnelheid, luchtvochtigheid))
        print(f"Gemiddelde: {totaal / dag}")



weerstation()