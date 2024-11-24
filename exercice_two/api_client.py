import requests

from common_files import APIClient, timestamp_to_date, ConfReader
from common_files.display_results import Display
from exercice_two.configuration_reader import TomlConfReader
from exercice_two.utils.handling_timestamps import (
    timestamp_range_for_the_next_fives_days,
)


class WeatherAPIClient(APIClient):
    """
    Classe permettant de communiquer avec l'API OpenWeatherMap.
    """

    def __init__(self, config_reader: ConfReader = TomlConfReader("exercice_two/configuration.toml")):
        self.config_reader = config_reader

    def fetch_data(self) -> dict:
        """
        Renvoie les données de prévisions météorologiques de l'API OpenWeatherMap pour la ville spécifiée.
        Renvoie le contenu de la réponse sous la forme d'un dictionnaire JSON, ou None en cas d'erreur.
        """
        api_url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {
            "q": self.config_reader.read_conf()['location']['city'],
            "appid": self.config_reader.read_conf()['api']['weather']['key'],
            "units": "metric",
            "lang": "fr",
            "exclude": "hourly,minutely,current,alerts",
        }
        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            raise Exception(
                f"Erreur lors de la requ te API OpenWeatherMap: {error}"
            ) from error


class WeatherDataProcessor:
    """
    Classe pour traiter les données météorologiques.
    """

    @staticmethod
    def find_min_max_temperature(
            timestamp_range: list, data_forecast: dict
    ) -> tuple[float, float]:
        """Renvoie les températures minimale et maximale pour une plage de timestamps."""
        min_temp = float("inf")
        max_temp = float("-inf")

        for day in data_forecast["list"]:
            if timestamp_range[1] > day["dt"] > timestamp_range[0]:
                min_temp = min(min_temp, day["main"]["temp"])
                max_temp = max(max_temp, day["main"]["temp"])
        return min_temp, max_temp


class DisplayWeatherRequestResults(Display):
    def __init__(self, client: WeatherAPIClient):
        self.client = client

    def print(self):
        """Affiche les prévisions des températures minimales et maximales pour les 5 prochains jours"""
        print(f"Forecasts for {self.client.config_reader.read_conf()['location']['city']} are:\n")
        for day in timestamp_range_for_the_next_fives_days():
            self._display_min_max_temperature_for_day(day)

    def _display_min_max_temperature_for_day(self, timestamp_range: list) -> None:
        """Affiche les températures minimales et maximales pour une plage de timestamp"""

        # Affiche le jour en toute lettre
        formatted_date = timestamp_to_date(timestamp_range[0], "%A")

        min_temp, max_temp = WeatherDataProcessor.find_min_max_temperature(
            timestamp_range, self.client.fetch_data()
        )

        print(
            f"{formatted_date}\n\t"
            f"minimum temperature: {min_temp}°C\n\t"
            f"maximum temperature: {max_temp}°C\n"
        )
