from unittest.mock import patch

from src.classes.cls_hh import HH


def test_get_api_hh(init_hh: HH) -> None:
    with patch("requests.get") as mock_requests:
        mock_requests.return_value.status_code = 200
        mock_requests.return_value.json.return_value = {"items": []}
        hh_vacancies = init_hh.load_vacancies("Python")
        assert hh_vacancies == []

    with patch("requests.get") as mock_requests:
        mock_requests.return_value.status_code = 400
        hh_vacancies = init_hh.load_vacancies("Python")
        assert hh_vacancies == []
