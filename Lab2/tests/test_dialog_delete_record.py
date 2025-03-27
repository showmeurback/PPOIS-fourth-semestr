import pytest
from MVC.view.dialog_delete_record import DeleteRecordDialog

def test_delete_record_dialog_creation():
    # Создание диалогового окна
    dialog = DeleteRecordDialog(None)
    assert dialog is not None
    dialog.destroy()