import pytest
from MVC.controller.main_controller import MainController
from MVC.model.database import Database
from MVC.model.record import Record

@pytest.fixture
def controller():
    db = Database(":memory:")
    for i in range(25):  # Добавляем 25 записей
        db.insert_record(Record(fio=f"Игрок {i}", composition="Основной", position="Нападающий", titles=i, sport_type="Футбол", rank="Профессионал"))
    controller = MainController()
    controller.db = db
    return controller

def test_pagination(controller):
    controller.records_per_page = 10
    controller.current_page = 1
    records = controller.get_paginated_records()
    assert len(records) == 10
    assert records[0].fio == "Игрок 0"

    controller.current_page = 2
    records = controller.get_paginated_records()
    assert len(records) == 10
    assert records[0].fio == "Игрок 10"

    controller.current_page = 3
    records = controller.get_paginated_records()
    assert len(records) == 5
    assert records[0].fio == "Игрок 20"