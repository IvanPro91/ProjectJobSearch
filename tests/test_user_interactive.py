from _pytest.capture import CaptureFixture

from src.classes.cls_vacancy import Vacancy
from src.user_interactive import (
    filter_vacancies,
    get_top_vacancies,
    get_vacancies_by_salary,
    print_vacancies,
    sort_vacancies,
)


def test_user_inter(capsys: CaptureFixture, init_vacancy: Vacancy) -> None:
    """Тесты"""
    data: list[Vacancy] = [init_vacancy]
    words = "python".split()
    assert filter_vacancies(data, words) == []

    assert get_vacancies_by_salary(data, "1-1000")[0].name == "Тестировщик (QA-инженер)"
    assert sort_vacancies(data)[0].id_vacancy == "119602010"
    assert get_top_vacancies(data, 1)[0].id_vacancy == "119602010"
    print_vacancies(data)
    read_out = capsys.readouterr()
    assert read_out.out == (
        "119602010 Тестировщик (QA-инженер) "
        "https://api.hh.ru/vacancies/119602010?host=hh.ru 1 - 10000 Знакомство с "
        "Postman и умение составлять API запросы. Знание основ HTML, CSS, JS, "
        "<highlighttext>Python</highlighttext>. Опыт написания тестовой документации "
        "(тест-кейсы...\n"
    )
