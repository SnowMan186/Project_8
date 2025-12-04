from typing import Optional
from datetime import date


class Vacancy:
    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description
        self.created_at = date.today()

    def __lt__(self, other):
        min_salary_self = self.extract_minimum_salary()
        min_salary_other = other.extract_minimum_salary()

        return min_salary_self < min_salary_other

    def extract_minimum_salary(self):
        try:
            salary_parts = self.salary.split('-')
            return float(salary_parts[0].replace(' ', '').replace('руб.', ''))
        except (IndexError, ValueError):
            return 0
