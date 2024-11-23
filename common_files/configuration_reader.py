from abc import ABC, abstractmethod


class ConfReader(ABC):

    @abstractmethod
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def read_conf(self):
        """
        Lire le fichier de configuration
        """
        pass
