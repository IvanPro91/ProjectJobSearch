from abc import ABC, abstractmethod
from typing import Any

import requests


class HhBase(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def load_vacancies(self, keyword: str) -> list: ...


class HH(HhBase):
    """
    Класс для работы с API HeadHunter
    Класс HhBase является родительским классом
    """

    __slots__ = ("__url", "__headers", "__params", "__vacancies")
    __url: str
    __headers: dict
    __params: dict
    __vacancies: list

    def __init__(self) -> None:
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []
        super().__init__()

    def load_vacancies(self, keyword: str) -> list[Any]:
        """Получение данных от сервера"""
        self.__params["text"] = keyword
        while self.__params.get("page") != 2:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code == 200:
                vacancies = response.json()["items"]
                self.__vacancies.extend(vacancies)
                self.__params["page"] += 1
        return self.__vacancies
