import unittest
from src.file_handlers import AbstractFileHandler, JSONSaver
from pathlib import Path
import os


class TestAbstractFileHandler(unittest.TestCase):
    def test_abstract_class_cannot_be_instantiated_directly(self):
        with self.assertRaises(TypeError):
            AbstractFileHandler()

    def test_subclass_without_methods_raises_type_error(self):
        class MySubClass(AbstractFileHandler):
            pass
        with self.assertRaises(TypeError):
            MySubClass()


class TestJSONSaver(unittest.TestCase):
    def setUp(self):
        self.filename = 'test_vacancies.json'
        self.saver = JSONSaver(self.filename)

    def tearDown(self):
        if Path(self.filename).exists():
            os.remove(self.filename)

    def test_add_vacancy_creates_new_file_if_missing(self):
        self.saver.add_vacancy({"title": "Test Job", "id": "unique-id"})
        self.assertTrue(Path(self.filename).exists())

    def test_add_vacancy_appends_to_existing_file(self):
        initial_data = {"title": "Initial Job", "id": "initial-id"}
        self.saver.add_vacancy(initial_data)
        second_data = {"title": "Second Job", "id": "second-id"}
        self.saver.add_vacancy(second_data)

        with open(self.filename, 'r') as file:
            content = file.read()
            self.assertIn('"title": "Initial Job"', content)
            self.assertIn('"title": "Second Job"', content)

    def test_delete_vacancy_removes_from_file(self):
        self.saver.add_vacancy({"title": "Job to Delete", "id": "delete-me"})
        self.saver.delete_vacancy("delete-me")

        with open(self.filename, 'r') as file:
            content = file.read()
            self.assertNotIn('"title": "Job to Delete"', content)

