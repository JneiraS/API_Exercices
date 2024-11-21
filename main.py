from exercice_one.api_client import display_iss_informations
from exercice_two.api_client import display_temperature_forecasts


def main():
    """
    Affiche les prévisions de température pour les 5 prochains jours,
    les coordonnées de l'ISS, ainsi que les astronautes sur l'ISS.
    """
    display_temperature_forecasts()
    display_iss_informations()


if __name__ == "__main__":
    main()
