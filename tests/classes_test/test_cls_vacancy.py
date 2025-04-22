from src.classes.cls_vacancy import Vacancy


def test_vacancy(init_vacancy: Vacancy, vacancy_data: dict) -> None:
    assert str(init_vacancy) == (
        "119602010 Тестировщик (QA-инженер) "
        "https://api.hh.ru/vacancies/119602010?host=hh.ru 1 - 10000 Знакомство с "
        "Postman и умение составлять API запросы. Знание основ HTML, CSS, JS, "
        "<highlighttext>Python</highlighttext>. Опыт написания тестовой документации "
        "(тест-кейсы..."
    )

    assert isinstance(Vacancy.create_vacancies([vacancy_data]), list)
