import requests

from common_files import APIClient, timestamp_to_date
from configuration_reader import TomlConfReader
from exercice_two.utils.handling_timestamps import timestamp_range_for_the_next_fives_days


class WeatherAPI(APIClient):
    """
    Classe permettant de communiquer avec l'API OpenWeatherMap.
    """
    configuration_reader = TomlConfReader('conf.toml')

    def __init__(self):
        self.city = WeatherAPI.configuration_reader.get_city()
        self.api_key = WeatherAPI.configuration_reader.get_api_key()

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
            "exclude": "hourly,minutely,current,alerts"
        }
        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            raise Exception(f"Erreur lors de la requ te API OpenWeatherMap: {error}") from error

    def _find_min_temp(self, timestamp_range: list) -> float:
        """
        Renvoie la température minimale pour une plage de timestamp,
        en cherchant dans les données de l'API OpenWeatherMap.
        """
        temp_min = []
        for day in self.fetch_data()["list"]:
            if timestamp_range[1] > day["dt"] > timestamp_range[0]:
                temp_min.append(day['main']['temp_min'])
        return min(temp_min)

    def _find_max_temp(self, timestamp_range: list) -> float:
        """
        Renvoie la température minimale pour une plage de timestamp,
        en cherchant dans les données de l'API OpenWeatherMap.
        """
        temp_min = []
        for day in self.fetch_data()["list"]:
            if timestamp_range[1] > day["dt"] > timestamp_range[0]:
                temp_min.append(day['main']['temp_min'])
        return max(temp_min)

    def display_min_max_temperature_for_day(self, timestamp_range: list) -> None:
        """Affiche les prévisions pour les 5 prochains jours"""
        formatted_date = timestamp_to_date(timestamp_range[0], '%A')
        min_temp = self._find_min_temp(timestamp_range)
        max_temp = self._find_max_temp(timestamp_range)
        print(f"Forecasts for {self.city} are:\n")
        print(f"{formatted_date}\n\t"
              f"minimum temperature: {min_temp}°C\n\t"
              f"maximum temperature: {max_temp}°C\n")


def display_temperature_forecasts():
    for day in timestamp_range_for_the_next_fives_days():
        WeatherAPI().display_min_max_temperature_for_day(day)



