import requests

from common_files import APIClient, timestamp_to_date
from exercice_two.configuration_reader import TomlConfReader

from exercice_two.utils.handling_timestamps import (
    timestamp_range_for_the_next_fives_days,
)


class WeatherAPIClient(APIClient):
    """
    Classe permettant de communiquer avec l'API OpenWeatherMap.
    """

    configuration_reader = TomlConfReader("exercice_two/configuration.toml")

    def __init__(self):
        self.city = WeatherAPIClient.configuration_reader.get_city()
        self.api_key = WeatherAPIClient.configuration_reader.get_api_key()

    def fetch_data(self) -> dict:
        """
        Renvoie les données de prévisions météorologiques de l'API OpenWeatherMap pour la ville spécifiée.
        Renvoie le contenu de la réponse sous la forme d'un dictionnaire JSON, ou None en cas d'erreur.
        """
        api_url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {
            "q": self.city,
            "appid": self.api_key,
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

    def _find_temp(self, timestamp_range: list, operation: str) -> float:
        """
        Renvoie la température min/max pour une plage de timestamp,
        en cherchant dans les données de l'API OpenWeatherMap.

        Args:
            timestamp_range: Liste contenant timestamp début et fin
            operation: 'min' ou 'max' pour spécifier l'opération
        """
        temp = float("inf") if operation == "min" else float("-inf")
        compare_func = min if operation == "min" else max

        for day in self.fetch_data()["list"]:
            if timestamp_range[1] > day["dt"] > timestamp_range[0]:
                temp = compare_func(temp, day["main"]["temp"])
        return temp

    def _find_min_temp(self, timestamp_range: list) -> float:
        return self._find_temp(timestamp_range, "min")

    def _find_max_temp(self, timestamp_range: list) -> float:
        return self._find_temp(timestamp_range, "max")

    def _display_min_max_temperature_for_day(self, timestamp_range: list) -> None:
        """Affiche les températures minimales et maximales pour une plage de timestamp"""

        # Affiche le jour en toute lettre
        formatted_date = timestamp_to_date(timestamp_range[0], "%A")

        print(
            f"{formatted_date}\n\t"
            f"minimum temperature: {self._find_min_temp(timestamp_range)}°C\n\t"
            f"maximum temperature: {self._find_max_temp(timestamp_range)}°C\n"
        )


def display_temperature_forecasts():
    """Affiche les prévisions des températures minimales et maximales pour les 5 prochains jours"""
    client = WeatherAPIClient()
    print(f"Forecasts for {client.city} are:\n")
    for day in timestamp_range_for_the_next_fives_days():
        client._display_min_max_temperature_for_day(day)
