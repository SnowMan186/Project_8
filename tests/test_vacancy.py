import unittest
from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):
    def test_create_vacancy(self):
        # Проверяем создание вакансии
        vacancy = Vacancy(
            "Python developer",
            "https://hh.ru/",
            "100000-150000 руб.",
            "Требуются знания Python",
        )
        self.assertEqual(vacancy.title, "Python developer")
        self.assertEqual(vacancy.url, "https://hh.ru/")
        self.assertEqual(vacancy.salary, "100000-150000 руб.")
        self.assertEqual(vacancy.description, "Требуются знания Python")

    def test_validation_error(self):
        # Проверяем ошибку при неверных данных
        with self.assertRaises(ValueError):
            Vacancy("", "", "", "")

    def test_sorting_by_salary(self):
        # Проверяем сортировку вакансий по зарплате
        vacancy1 = Vacancy(
            "Junior Python",
            "https://hh.ru/vacancy/1",
            "60000-80000 руб.",
            "Опыт работы от 1 года",
        )
        vacancy2 = Vacancy(
            "Middle Python",
            "https://hh.ru/vacancy/2",
            "100000-120000 руб.",
            "Опыт работы от 3 лет",
        )
        vacancy3 = Vacancy(
            "Senior Python",
            "https://hh.ru/vacancy/3",
            "150000-200000 руб.",
            "Опыт работы от 5 лет",
        )

        vacancies = [vacancy1, vacancy2, vacancy3]
        sorted_vacancies = sorted(vacancies)
        expected_order = [vacancy1, vacancy2, vacancy3]
        self.assertListEqual(sorted_vacancies, expected_order)

    def test_minimum_salary_extraction(self):
        # Проверяем правильное извлечение минимальной зарплаты
        vacancy = Vacancy(
            "Python developer",
            "https://hh.ru/",
            "100000-150000 руб.",
            "Требуются знания Python",
        )
        extracted_salary = vacancy.extract_minimum_salary()
        self.assertEqual(extracted_salary, 100000)

    def test_zero_salary_if_no_data(self):
        # Проверка случая отсутствия данных о зарплате
        vacancy = Vacancy(
            "Python developer", "https://hh.ru/", "-", "Требуются знания Python"
        )
        extracted_salary = vacancy.extract_minimum_salary()
        self.assertEqual(extracted_salary, 0)


if __name__ == "__main__":
    unittest.main()
