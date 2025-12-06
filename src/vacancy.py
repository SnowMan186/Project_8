from datetime import date


class Vacancy:
    def __init__(self, title, url, salary, description):
        self.validate_data(title, url, salary, description)
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description
        self.created_at = date.today()

    def validate_data(self, title, url, salary, description):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Название вакансии должно быть непустой строкой.")
        if not isinstance(url, str) or not url.strip():
            raise ValueError("URL вакансии должен быть непустой строкой.")
        if not isinstance(salary, str):
            raise ValueError("Значение зарплаты должно быть строкой.")
        if not isinstance(description, str) or not description.strip():
            raise ValueError("Описание вакансии должно быть непустой строкой.")

    def __lt__(self, other):
        min_salary_self = self.extract_minimum_salary()
        min_salary_other = other.extract_minimum_salary()
        return min_salary_self < min_salary_other

    def extract_minimum_salary(self):
        try:
            parts = self.salary.split("-")
            return float(parts[0].replace(" ", "").replace("руб.", ""))
        except (IndexError, ValueError):
            return 0
