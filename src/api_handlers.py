from abc import ABC, abstractmethod
import requests
from typing import Dict, Any, List, Optional


class AbstractJobApi(ABC):
    @abstractmethod
    def _connect(self) -> requests.Response:
        """Проверяет доступность API."""
        pass

    @abstractmethod
    def get_vacancies(
        self, text: str = "", area: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """Получает вакансии по указанному ключевому слову и области."""
        pass


class HeadHunterAPI(AbstractJobApi):
    _BASE_URL = "https://api.hh.ru/"

    def _connect(self) -> requests.Response:
        """Подключается к API и проверяет доступность."""
        response = requests.get(self._BASE_URL)
        if response.status_code != 200:
            raise ConnectionError(
                f"Не удалось подключиться к API. Код: {response.status_code}"
            )
        return response

    def get_vacancies(
        self, text: str = "", area: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """Получает вакансии по указанному ключевому слову и области."""
        self._connect()  # Проверяем подключение
        endpoint = "/vacancies"
        params = {"text": text}
        if area:
            params["area"] = area
        response = requests.get(self._BASE_URL + endpoint, params=params)
        if response.status_code == 200:
            return response.json()["items"]
        else:
            return []
