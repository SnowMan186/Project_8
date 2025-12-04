import unittest
from src.api_handlers import AbstractJobApiHandler, HeadHunterAPI
from unittest.mock import patch, Mock


class ConcreteJobApiHandler(AbstractJobApiHandler):
    def connect(self):
        pass

    def get_vacancies(self, keyword):
        pass


class TestAbstractJobApiHandler(unittest.TestCase):
    def test_abstract_class_cannot_be_instantiated_directly(self):
        with self.assertRaises(TypeError):
            AbstractJobApiHandler()

    def test_concrete_class_can_be_instantiated(self):
        instance = ConcreteJobApiHandler()
        self.assertIsInstance(instance, AbstractJobApiHandler)


class TestHeadHunterAPI:
    @patch('requests.get')
    def test_get_vacancies_returns_valid_response(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'items': ['mocked_item']}
        mock_get.return_value = mock_response

        hh_api = HeadHunterAPI()
        result = hh_api.get_vacancies("Python")
        assert result == ['mocked_item']

    @patch('requests.get')
    def test_get_vacancies_raises_connection_error_on_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        hh_api = HeadHunterAPI()
        with pytest.raises(Exception):
            hh_api.get_vacancies("Python")
