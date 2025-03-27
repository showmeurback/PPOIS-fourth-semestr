import pytest
from MVC.controller.delete_record_controller import DeleteRecordController
from MVC.model.database import Database
from MVC.model.record import Record

@pytest.fixture
def db():
    db = Database(":memory:")
    db.insert_record(Record(fio="Иванов Иван", composition="Основной", position="Нападающий", titles=5, sport_type="Футбол", rank="Профессионал"))
    yield db
    db.conn.close()

@pytest.fixture
def controller(db):
    return DeleteRecordController(db)

