import json
from pathlib import Path
from abc import ABC, abstractmethod


class AbstractFileHandler(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: dict):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id: str):
        pass

    @abstractmethod
    def get_vacancies(self, filters=None):
        pass


class JSONSaver(AbstractFileHandler):
    def __init__(self, filename="vacancies.json"):
        self._filename = filename
        self._path = Path(filename)

    def add_vacancy(self, vacancy: dict):
        existing_data = []
        if self._path.exists():
            with open(self._path, "r") as file:
                existing_data.extend(json.load(file))

        new_data = {**vacancy}
        existing_data.append(new_data)

        with open(self._path, "w") as file:
            json.dump(existing_data, file, indent=4)

    def delete_vacancy(self, vacancy_id: str):
        if not self._path.exists():
            return None

        with open(self._path, "r+") as file:
            data = json.load(file)
            updated_data = [v for v in data if v.get("id") != vacancy_id]
            file.seek(0)
            json.dump(updated_data, file, indent=4)
            file.truncate()

    def get_vacancies(self, filters=None):
        if not self._path.exists():
            return []

        with open(self._path, "r") as file:
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
