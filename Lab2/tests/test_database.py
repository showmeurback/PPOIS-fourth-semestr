import pytest
from MVC.model.database import Database
from MVC.model.record import Record

@pytest.fixture
def db():
    db = Database(":memory:")  # Используем временную базу данных в памяти
    yield db
    db.conn.close()

def test_create_table(db):
    cursor = db.conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='records'")
    result = cursor.fetchone()
    assert result[0] == "records"

def test_insert_and_retrieve_records(db):
    record = Record(fio="Петров Петр", composition="Основной", position="Защитник", titles=3, sport_type="Хоккей", rank="Любитель")
    db.insert_record(record)
    records = db.get_records()
    assert len(records) == 1
    assert records[0].fio == "Петров Петр"

def test_search_records(db):
    record1 = Record(fio="Иванов Иван", composition="Основной", position="Нападающий", titles=5, sport_type="Футбол", rank="Профессионал")
    record2 = Record(fio="Петров Петр", composition="Основной", position="Защитник", titles=3, sport_type="Хоккей", rank="Любитель")
    db.insert_record(record1)
    db.insert_record(record2)
    results = db.search_records(criteria={"fio": "Иванов"})
    assert len(results) == 1
    assert results[0].fio == "Иванов Иван"

def test_delete_records(db):
    record = Record(fio="Иванов Иван", composition="Основной", position="Нападающий", titles=5, sport_type="Футбол", rank="Профессионал")
    db.insert_record(record)
    db.delete_records(criteria={"fio": "Иванов"})
    records = db.get_records()
    assert len(records) == 0