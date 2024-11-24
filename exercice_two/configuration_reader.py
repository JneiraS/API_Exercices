from typing import Any

import toml

from common_files import ConfReader


class TomlConfReader(ConfReader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_conf(self) -> dict[str, Any]:
        """Lire un fichier de configuration écrit au format TOML."""
        with open(self.file_path, "r", encoding="unicode_escape") as f:
            return toml.load(f)
