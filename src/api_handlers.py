from abc import ABC, abstractmethod
import requests


class AbstractJobApi(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(AbstractJobApi):
    BASE_URL = "https://api.hh.ru/"

    def connect(self):
        pass

    def get_vacancies(self, text="", keyword="", area=None):
        # Простая реализация метода получения вакансий
        endpoint = "/vacancies"
        params = {"text": keyword}
        response = requests.get(self.BASE_URL + endpoint, params=params)
        if response.status_code == 200:
            return response.json()["items"]
        else:
            return []
