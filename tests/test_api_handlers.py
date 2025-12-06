import unittest
from src.api_handlers import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    def setUp(self):
        self.api_handler = HeadHunterAPI()

    def test_get_vacancies(self):
        # Проверяем успешное получение вакансий
        vacancies = self.api_handler.get_vacancies(text="Python разработчик")
        self.assertIsInstance(vacancies, list)
        self.assertGreater(len(vacancies), 0)

    def test_get_vacancies_with_area(self):
        # Проверяем получение вакансий с указанием региона
        moscow_area_id = 1  # ID Москвы на hh.ru
        vacancies = self.api_handler.get_vacancies(area=moscow_area_id)
        self.assertIsInstance(vacancies, list)
        self.assertGreater(len(vacancies), 0)

    def test_connect(self):
        # Проверяем соединение с API
        self.api_handler.connect()
        # Нет исключений - значит успешно подключились

    def test_get_vacancies_empty_text(self):
        # Проверяем получение вакансий без текста
        vacancies = self.api_handler.get_vacancies()
        self.assertIsInstance(vacancies, list)
        self.assertGreater(len(vacancies), 0)


if __name__ == "__main__":
    unittest.main()
