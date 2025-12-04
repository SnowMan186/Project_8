from abc import ABC, abstractmethod
import requests


class AbstractJobApiHandler(ABC):
    """Абстрактный класс для работы с API сайтов вакансий."""

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(AbstractJobApiHandler):
    """Конкретная реализация для работы с hh.ru"""

    def __init__(self, base_url='https://api.hh.ru'):
        self.base_url = base_url  # Базовый адрес API HeadHunter
        self.vacancies = []  # Список для хранения вакансий

    def _connect(self):
        pass  # Реализация заглушки, подтверждающая успешное подключение

    def get_vacancies(self, text='', area=None, per_page=100):
        """
        Отправляет запрос к API HeadHunter и получает вакансии.
        :param text: Текстовый запрос (должность, специализацию)
        :param area: ID региона (можно оставить None, если не важен регион)
        :param per_page: Кол-во вакансий на страницу (до 100)
        :return: Возвращает список вакансий
        """
        endpoint = '/vacancies'
        params = {
            'text': text,  # Ключевое слово для поиска (например, должность)
            'area': area,  # Регион поиска (если нужен)
            'per_page': per_page  # Максимальное количество вакансий на странице
        }

        response = requests.get(self.base_url + endpoint, params=params)
        if response.status_code == 200:
            data = response.json()
            self.vacancies = data['items']  # Берем список вакансий
            return self.vacancies
        else:
            print(f"Ошибка при запросе к API: {response.status_code}")
            return []

    def save_to_json(self, filename='vacancies.json'):
        """
        Сохраняет собранные вакансии в JSON-файл.
        :param filename: Имя файла для сохранения
        """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.vacancies, file, ensure_ascii=False, indent=4)
        print(f"Вакансии сохранены в файл {filename}")
