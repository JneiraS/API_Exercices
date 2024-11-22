from exercice_one.api_client import DisplayISSInformations, IssLocationAPIClient, IssAstronautsAPIClient
from exercice_two.api_client import DisplayWeatherRequestResults, \
    WeatherAPIClient


def main():
    """
    Affiche les prévisions de température pour les 5 prochains jours,
    les coordonnées de l'ISS, ainsi que les astronautes sur l'ISS.
    """
    weather_client = WeatherAPIClient()
    iss_location = IssLocationAPIClient()
    iss_astronauts = IssAstronautsAPIClient()

    DisplayWeatherRequestResults(weather_client).print()
    DisplayISSInformations(iss_location).print()
    DisplayISSInformations(iss_astronauts).print()


if __name__ == "__main__":
    main()
