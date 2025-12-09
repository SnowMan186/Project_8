import json
from pathlib import Path
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional


class AbstractFileHandler(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: dict) -> None:
        """Добавляет вакансию в файл."""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id: str) -> bool:
        """Удаляет вакансию из файла."""
        pass

    @abstractmethod
    def get_vacancies(self, filters: Optional[dict] = None) -> List[Dict[str, Any]]:
        """Получает вакансии из файла с возможностью фильтрации."""
        pass


class JSONSaver(AbstractFileHandler):
    def __init__(self, filename: str = "vacancies.json"):
        self.__filename = filename  # Приватный атрибут
        self.__path = Path(filename)

    def add_vacancy(self, vacancy: dict) -> None:
        """Добавляет вакансию в файл, предотвращая дублирование."""
        existing_data = []
        if self.__path.exists():
            with open(self.__path, "r") as file:
                existing_data.extend(json.load(file))

        # Проверка на дублирование (по URL)
        if any(v.get("url") == vacancy.get("url") for v in existing_data):
            return  # Вакансия уже существует

        existing_data.append(vacancy)
        with open(self.__path, "w") as file:
            json.dump(existing_data, file, indent=4)

    def delete_vacancy(self, vacancy_id: str) -> bool:
        """Удаляет вакансию по уникальному идентификатору."""
        if not self.__path.exists():
            return False

        with open(self.__path, "r+") as file:
            data = json.load(file)
            updated_data = [v for v in data if v.get("id") != vacancy_id]
            file.seek(0)
            json.dump(updated_data, file, indent=4)
            file.truncate()
        return True

    def get_vacancies(self, filters: Optional[dict] = None) -> List[Dict[str, Any]]:
        """Получает вакансии из файла с поддержкой фильтрации."""
        if not self.__path.exists():
            return []

        with open(self.__path, "r") as file:
            data = json.load(file)

        if filters is None:
            return data
        else:
            return list(
                filter(
                    lambda x: all(
                        str(x.get(k)).lower() == str(v).lower()
                        for k, v in filters.items()
                    ),
                    data,
                )
            )
