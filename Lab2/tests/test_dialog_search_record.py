import pytest
from MVC.view.dialog_search_record import SearchRecordDialog

def test_search_record_dialog_creation():
    # Создание диалогового окна
    dialog = SearchRecordDialog(None)
    assert dialog is not None
    dialog.destroy()