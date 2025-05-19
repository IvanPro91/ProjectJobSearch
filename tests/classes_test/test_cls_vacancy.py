from src.classes.cls_vacancy import Vacancy


def test_vacancy(init_vacancy: Vacancy, vacancy_data: dict) -> None:
    assert str(init_vacancy) == (
        "{'id_vacancy': '119602010', 'name': 'Тестировщик (QA-инженер)', 'url': "
        "'https://api.hh.ru/vacancies/119602010?host=hh.ru', 'company_name': 'name', "
        "'company_id': 1, 'salary_from': 1, 'salary_to': 10000, 'requirement': "
        "'Знакомство с Postman и умение составлять API запросы. Знание основ HTML, "
        "CSS, JS, <highlighttext>Python</highlighttext>. Опыт написания тестовой "
        "документации (тест-кейсы...'}"
    )

    assert isinstance(Vacancy.create_vacancies([vacancy_data]), list)
