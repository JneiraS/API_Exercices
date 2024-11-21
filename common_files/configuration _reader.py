from abc import ABC, abstractmethod



class ConfReader(ABC):
    @abstractmethod
    def read_conf(self):
        """
        Lire le fichier de configuration
        """
        pass





