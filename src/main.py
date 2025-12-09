from src.api_handlers import HeadHunterAPI
from src.vacancy import Vacancy
from src.file_handlers import JSONSaver
from typing import Dict, Any, List


def fetch_and_save_vacancies(keyword: str):
    """
    Загружает вакансии с hh.ru и сохраняет их в файл.

    Args:
        keyword: Ключевое слово для поиска вакансий
    """
    hh_api = HeadHunterAPI()
    raw_vacancies = hh_api.get_vacancies(keyword)

    vacancies = [
        Vacancy(
            item["name"],
            item["alternate_url"],
            str(item.get("salary", {}).get("to", "0")),
            item["snippet"]["requirement"],
        )
        for item in raw_vacancies
    ]

    saver = JSONSaver()
    for vacancy in vacancies:
        saver.add_vacancy(vars(vacancy))


def show_top_vacancies(n: int):
    """
    Показывает топ-N вакансий по зарплате.

    Args:
        n: Количество вакансий для отображения
    """
    saver = JSONSaver()
    data = saver.get_vacancies()
    sorted_data = sorted(
        data,
        key=lambda x: float(x.get("salary", "0").split("-")[0].strip()),
        reverse=True,
    )
    print(f"Топ-{n} вакансий:")
    for i, vacancy in enumerate(sorted_data[:n]):
        print(
            f"{i + 1}. Название: {vacancy['title']} | Зарплата: {vacancy.get('salary', '-')}"
        )


def filter_vacancies(filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Возвращает список вакансий, соответствующих фильтрам.

    Args:
        filters: Словарь с параметрами фильтрации
    Returns:
        Список вакансий
    """
    saver = JSONSaver()
    return saver.get_vacancies(filters)


def main():
    while True:
        print("\nМеню:")
        print("1. Загрузить новые вакансии")
        print("2. Показать топ-N вакансий")
        print("3. Фильтрация вакансий")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            fetch_and_save_vacancies(keyword)
        elif choice == "2":
            n = int(input("Введите число N для отображения топ-вакансий: "))
            show_top_vacancies(n)
        elif choice == "3":
            word_filter = input("Введите фильтр по названию вакансии: ")
            results = filter_vacancies({"title": word_filter})
            print(f"Вакансии с названием '{word_filter}' ({len(results)}):")
            for result in results:
                print(result["title"])
        elif choice == "4":
            break
        else:
            print("Некорректный выбор!")


if __name__ == "__main__":
    main()
