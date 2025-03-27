import pytest
from MVC.controller.main_controller import MainController
from MVC.model.database import Database
from MVC.model.record import Record

@pytest.fixture
def db():
    # Создаём новую временную базу данных для каждого теста
    db = Database(":memory:")
    yield db
    db.conn.close()

@pytest.fixture
def controller(db):
    # Передаём временную базу данных в контроллер
    controller = MainController()
    controller.db = db
    return controller