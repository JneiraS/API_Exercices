from datetime import datetime

import requests

import common_files as cf


class IssLocationAPIClient(cf.APIClient):
    def __init__(self):
        self.url_location_api = 'http://api.open-notify.org/iss-now.json'

    def fetch_data(self) -> dict:
        """
        Renvoie les données de la réponse de l'API Open Notify.
        Renvoie un dictionnaire JSON, ou None en cas d'erreur.
        """
        try:
            response = requests.get(self.url_location_api)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erreur lors de la requ te API Open Notify: {e}") from e


def timestamp_to_date(timestamp: int) -> str:
    """Convertit un timestamp en une date au format 'AAAA-MM-JJ HH:MM:SS'."""
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
