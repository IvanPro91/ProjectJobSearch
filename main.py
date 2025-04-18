from src.classes.cls_file_handler import FileHandlerJob
from src.classes.cls_hh import HH
from src.classes.cls_vacancy import Vacancy
from src.user_interactive import (
    filter_vacancies,
    get_top_vacancies,
    get_vacancies_by_salary,
    print_vacancies,
    sort_vacancies,
)

hh_api = HH()
file_handler = FileHandlerJob()


# Функция для взаимодействия с пользователем
def user_interaction() -> None:
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    hh_vacancies = hh_api.load_vacancies(search_query)
    print(hh_vacancies)
    vacancies_list = Vacancy.get_vacancy(hh_vacancies)
    file_handler.add_vacancy(vacancies_list)

    file_handler.delete_vacancy(vacancies_list[0])
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
