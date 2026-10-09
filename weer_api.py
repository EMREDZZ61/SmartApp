#Sprint 3: huidig weer ophalen via de Open-Meteo API (Utrecht).
import json
import urllib.request

URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=52.09&longitude=5.12"
    "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    "&wind_speed_unit=ms"
)


def haal_huidig_weer():
    #Geeft een dictionary met het huidige weer terug, of None als het niet lukt.
    try:
        with urllib.request.urlopen(URL, timeout=10) as antwoord:
            data = json.loads(antwoord.read().decode("utf-8"))
        huidig = data["current"]
        return {
            "temperatuur": float(huidig["temperature_2m"]),
            "windsnelheid": float(huidig["wind_speed_10m"]),
            "vochtigheid": int(round(huidig["relative_humidity_2m"])),
        }
    except OSError:
        # Geen internet, timeout of server niet bereikbaar
        print("Fout: geen verbinding met Open-Meteo. Controleer je internet.")
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        print("Fout: onverwacht antwoord van Open-Meteo.")
    return None