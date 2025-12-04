import unittest
from src.vacancy import Vacancy
from datetime import date


class TestVacancy(unittest.TestCase):
    def test_vacancy_attributes_are_correctly_set(self):
        vacancy = Vacancy("Software Engineer", "https://hh.ru/vacancy/123456",
                          "100000-150000 руб.", "Требуются знания Python и Django")
        self.assertEqual(vacancy.title, "Software Engineer")
        self.assertEqual(vacancy.url, "https://hh.ru/vacancy/123456")
        self.assertEqual(vacancy.salary, "100000-150000 руб.")
        self.assertEqual(vacancy.description, "Требуются знания Python и Django")
        self.assertEqual(vacancy.created_at, date.today())

    def test_validation_fails_with_empty_fields(self):
        with self.assertRaises(ValueError):
            Vacancy("", "", "", "")

    def test_comparison_between_vacancies_based_on_salary(self):
        vacancy1 = Vacancy("Junior Dev", "https://hh.ru/junior", "50000-70000 руб.",
                           "Нужна помощь начинающим специалистам")
        vacancy2 = Vacancy("Senior Dev", "https://hh.ru/senior", "150000-200000 руб.",
                           "Необходим опыт работы от 5 лет")

        self.assertLess(vacancy1, vacancy2)
