import pytest
from MVC.view.tree_view import TreeViewWindow
from MVC.controller.tree_view_controller import TreeViewController
from MVC.model.database import Database
from MVC.model.record import Record

@pytest.fixture
def db():
    db = Database(":memory:")
    db.insert_record(Record(fio="Иванов Иван", composition="Основной", position="Нападающий", titles=5, sport_type="Футбол", rank="Профессионал"))
    yield db
    db.conn.close()

@pytest.fixture
def tree_controller(db):
    return TreeViewController(db)

def test_tree_view_creation(tree_controller):
    # Создание окна древовидного представления
    tree_view = TreeViewWindow(tree_controller)
    assert tree_view is not None
    tree_view.destroy()