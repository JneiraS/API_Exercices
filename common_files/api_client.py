# -*- coding: utf-8 -*-

"""Classes abstraites pour gérer les APIs"""

from abc import ABC, abstractmethod


class APIClient(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fetch_data(self):
        """
        Renvoie les données de la réponse de l'API.
        Le contenu des données renvoyées dépend de l'API.
        """
        pass
