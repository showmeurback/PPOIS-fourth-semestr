import pytest
from MVC.view.dialog_add_record import AddRecordDialog

def test_add_record_dialog_creation():
    # Создание диалогового окна
    dialog = AddRecordDialog(None)
    assert dialog is not None
    dialog.destroy()