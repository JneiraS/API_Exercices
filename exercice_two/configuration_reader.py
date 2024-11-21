from typing import Any

import toml

from common_files import ConfReader


class TomlConfReader(ConfReader):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_conf(self) -> dict[str, Any]:
        """Lire un fichier de configuration écrit au format TOML."""
        with open(self.file_path, 'r', encoding='unicode_escape') as f:
            return toml.load(f)

    def get_api_key(self) -> str:
        """
        Renvoie la clé API OpenWeatherMap lue depuis le fichier de configuration.
        :return: La clé API OpenWeatherMap
        """
        conf = self.read_conf()
        return conf['api']['weather']['key']

    def get_city(self) -> str:
        """
        Renvoie la ville lue depuis le fichier de configuration.
        :return: La ville
        """
        conf = self.read_conf()
        return conf['location']['city']