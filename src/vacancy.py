from datetime import date
from functools import total_ordering


@total_ordering
class Vacancy:
    __slots__ = ("title", "url", "salary", "description", "created_at")

    def __init__(self, title: str, url: str, salary: str, description: str):
        """
        Инициализирует экземпляр вакансии.

        Args:
            title: Название вакансии
            url: URL вакансии
            salary: Зарплата
            description: Описание вакансии
        """
        self._validate_data(title, url, salary, description)
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description
        self.created_at = date.today()

    def _validate_data(
        self, title: str, url: str, salary: str, description: str
    ) -> None:
        """
        Проверяет корректность входных данных.

        Raises:
            ValueError: Если данные некорректны.
        """
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Название вакансии должно быть непустой строкой.")
        if not isinstance(url, str) or not url.strip():
            raise ValueError("URL вакансии должен быть непустой строкой.")
        if not isinstance(salary, str):
            raise ValueError("Значение зарплаты должно быть строкой.")
        if not isinstance(description, str) or not description.strip():
            raise ValueError("Описание вакансии должно быть непустой строкой.")

    def __eq__(self, other: object) -> bool:
        """Проверяет равенство вакансий по минимальной зарплате."""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.extract_minimum_salary() == other.extract_minimum_salary()

    def __lt__(self, other: object) -> bool:
        """Сравнивает вакансии по минимальной зарплате."""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.extract_minimum_salary() < other.extract_minimum_salary()

    def extract_minimum_salary(self) -> float:
        """Извлекает минимальное значение зарплаты."""
        try:
            parts = self.salary.split("-")
            return float(parts[0].replace(" ", "").replace("руб.", ""))
        except (IndexError, ValueError):
            return 0
