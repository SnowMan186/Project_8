import os
import unittest
from src.file_handlers import JSONSaver


class TestJSONSaver(unittest.TestCase):
    def setUp(self):
        self.saver = JSONSaver()
        self.test_file_name = "test_vacancies.json"
        self.saver._filename = self.test_file_name
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

    def tearDown(self):
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

    def test_add_vacancy(self):
        # Добавляем вакансию
        vacancy = {"id": "1", "title": "Python developer"}
        self.saver.add_vacancy(vacancy)
        if os.path.exists(self.test_file_name):
            with open(self.test_file_name, "r") as f:
                content = f.read()
                self.assertIn('"title": "Python developer"', content)

    def test_delete_vacancy(self):
        # Убедимся, что удаление работающее
        vacancy = {"id": "1", "title": "Python developer"}
        self.saver.add_vacancy(vacancy)
        self.saver.delete_vacancy("1")
        if os.path.exists(self.test_file_name):
            with open(self.test_file_name, "r") as f:
                content = f.read()
                self.assertNotIn('"title": "Python developer"', content)

    def test_get_vacancies(self):
        # Проверяем получение всех вакансий
        vacancy1 = {"id": "1", "title": "Python developer"}
        vacancy2 = {"id": "2", "title": "JavaScript developer"}
        self.saver.add_vacancy(vacancy1)
        self.saver.add_vacancy(vacancy2)
        vacancies = self.saver.get_vacancies()
        self.assertEqual(len(vacancies), 2)

    def test_filtered_get_vacancies(self):
        # Проверяем фильтрацию по данным
        vacancy1 = {"id": "1", "title": "Python developer"}
        vacancy2 = {"id": "2", "title": "JavaScript developer"}
        self.saver.add_vacancy(vacancy1)
        self.saver.add_vacancy(vacancy2)
        filtered_vacancies = self.saver.get_vacancies({"title": "Python"})
        self.assertEqual(len(filtered_vacancies), 1)
