import requests

import common_files as cf
from common_files.display_results import Display
from common_files.utils.hanging_timestamps_format import timestamp_to_date


class IssLocationAPIClient(cf.APIClient):
    """
    Classe pour obtenir les coordonnées de l'ISS.
    """

    def __init__(self):
        self.url_api = "http://api.open-notify.org/iss-now.json"

    def fetch_data(self) -> dict:
        """Renvoie les données de la réponse de l'API Open Notify."""
        try:
            response = requests.get(self.url_api)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erreur lors de la requ te API Open Notify: {e}") from e


class IssAstronautsAPIClient(cf.APIClient):
    """Classe pour obtenir les astronautes dans l'ISS."""

    def __init__(self):
        self.url_api = "http://api.open-notify.org/astros.json"

    def fetch_data(self) -> dict:
        try:
            response = requests.get(self.url_api)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erreur lors de la requête API Open Notify: {e}") from e


class DisplayISSInformations(Display):
    """Classe pour afficher les informations de l'ISS."""

    def __init__(self, client: IssLocationAPIClient | IssAstronautsAPIClient):
        self.client = client

    def print(self) -> None:
        """Affiche les informations de l'ISS, en fonction du type de client."""
        data: dict = self.client.fetch_data()

        if isinstance(self.client, IssLocationAPIClient):
            self._display_iss_location(data)

        if isinstance(self.client, IssAstronautsAPIClient):
            self._display_astronauts(data)

    def _display_iss_location(self, data: dict):
        timestamp: int = data["timestamp"]
        iss_position: dict = data["iss_position"]
        print(
            f"Coordonnées de l'ISS à {timestamp_to_date(timestamp, '%H:%M:%S le %d-%m-%Y')}:"
            f" latitude={iss_position['latitude']}, longitude={iss_position['longitude']}."
        )

    def _display_astronauts(self, data: dict):
        people: list = data.get("people", [])
        count: int = sum(1 for person in people if person["craft"] == "ISS")
        print(f"Il y actuellement {count} astronautes sur l'ISS:")
        for person in people:
            if person["craft"] == "ISS":
                print(f"\t{person['name']}")
