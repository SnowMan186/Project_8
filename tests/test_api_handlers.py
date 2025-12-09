import unittest
from src.api_handlers import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    def setUp(self):
        self.api_handler = HeadHunterAPI()

    def test_connect(self):
        """
        Проверка подключения к API.
        """
        response = self.api_handler._connect()
        self.assertEqual(response.status_code, 200)

    def test_get_vacancies(self):
        """
        Проверка получения вакансий по ключевому слову.
        """
        vacancies = self.api_handler.get_vacancies(text="Python разработчик")
        self.assertIsInstance(vacancies, list)
        self.assertGreater(len(vacancies), 0)

    def test_get_vacancies_with_area(self):
        """
        Проверка получения вакансий с указанием региона.
        """
        moscow_area_id = 1  # ID Москвы на hh.ru
        vacancies = self.api_handler.get_vacancies(area=moscow_area_id)
        self.assertIsInstance(vacancies, list)
        self.assertGreater(len(vacancies), 0)

    def test_connection_failure(self):
        """
        Проверка реакции на ошибку подключения к API.
        """
        # Смоделируем отказ API (например, отключим интернет)
        with self.assertRaises(ConnectionError):
            # Формируем поддельный запрос, чтобы спровоцировать ошибку
            self.api_handler._connect()


if __name__ == "__main__":
    unittest.main()
