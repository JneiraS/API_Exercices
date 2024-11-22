from abc import ABC, abstractmethod

from common_files import APIClient


class Display(ABC):

    @abstractmethod
    def __init__(self, client: APIClient):
        self.client = client

    @abstractmethod
    def print(self):
        pass
