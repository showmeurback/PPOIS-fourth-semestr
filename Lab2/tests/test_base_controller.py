import pytest
from MVC.controller.base_controller import BaseController
from MVC.model.database import Database

@pytest.fixture
def db():
    db = Database(":memory:")
    yield db
    db.conn.close()

@pytest.fixture
def base_controller(db):
    return BaseController(db)

def test_base_controller_initialization(base_controller):
    # Проверка инициализации базового контроллера
    assert base_controller.db is not None