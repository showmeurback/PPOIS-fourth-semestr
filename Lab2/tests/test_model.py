import pytest
from MVC.model.record import Record

def test_record_creation():
    record = Record(fio="Иванов Иван", composition="Основной", position="Нападающий", titles=5, sport_type="Футбол", rank="Профессионал")
    assert record.fio == "Иванов Иван"
    assert record.composition == "Основной"
    assert record.position == "Нападающий"
    assert record.titles == 5
    assert record.sport_type == "Футбол"
    assert record.rank == "Профессионал"

def test_record_equality():
    record1 = Record(fio="Иванов Иван", composition="Основной", position="Нападающий", titles=5, sport_type="Футбол", rank="Профессионал")
    record2 = Record(fio="Иванов Иван", composition="Основной", position="Нападающий", titles=5, sport_type="Футбол", rank="Профессионал")
    assert record1 == record2