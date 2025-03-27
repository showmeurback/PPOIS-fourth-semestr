import pytest
from MVC.controller.add_record_controller import AddRecordController
from MVC.model.database import Database
from MVC.model.record import Record

@pytest.fixture
def db():
    db = Database(":memory:")
    yield db
    db.conn.close()

@pytest.fixture
def controller(db):
    return AddRecordController(db)