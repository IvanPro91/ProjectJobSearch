import os

from src.classes.cls_file_handler import FileHandlerJob
from src.classes.cls_vacancy import Vacancy


def test_file_handler(init_file_handler: FileHandlerJob, init_vacancy: Vacancy) -> None:
    assert os.path.exists(init_file_handler.filename)
    init_file_handler.write([init_vacancy.to_dict()])
    init_file_handler.delete_vacancy(init_vacancy)
    init_file_handler.add_vacancy([init_vacancy])
