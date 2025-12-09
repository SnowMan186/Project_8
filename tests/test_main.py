import unittest
from src.main import fetch_and_save_vacancies, show_top_vacancies, filter_vacancies
from src.file_handlers import JSONSaver


class TestMainFunctions(unittest.TestCase):
    def test_fetch_and_save_vacancies(self):
        # Тестируем сбор вакансий и сохранение
        fetch_and_save_vacancies("Python разработчик")

    def test_show_top_vacancies(self):
        # Заполняем некоторые тестовые вакансии
        saver = JSONSaver()
        saver.add_vacancy(
            {
                "id": "1",
                "title": "Senior Python Dev",
                "url": "https://hh.ru/",
                "salary": "150000-200000 руб.",
                "description": "Опыт работы 5 лет",
            }
        )
        saver.add_vacancy(
            {
                "id": "2",
                "title": "Junior Python Dev",
                "url": "https://hh.ru/",
                "salary": "60000-80000 руб.",
                "description": "Без опыта",
            }
        )
        # И показываем топ-1 вакансию
        show_top_vacancies(1)

    def test_filter_vacancies(self):
        # Проверяем фильтрацию вакансий
        results = filter_vacancies({"title": "Python"})
        self.assertGreater(len(results), 0)
