import pytest
from MVC.model.xml_handler import XMLWriter, XMLReader
from MVC.model.record import Record
import os

@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test.xml"

def test_save_to_xml(temp_file):
    records = [
        Record(fio="Иванов Иван", composition="Основной", position="Нападающий", titles=5, sport_type="Футбол", rank="Профессионал"),
        Record(fio="Петров Петр", composition="Основной", position="Защитник", titles=3, sport_type="Хоккей", rank="Любитель")
    ]
    XMLWriter.save_to_xml(records, temp_file)
    assert os.path.exists(temp_file)

def test_load_from_xml(temp_file):
    records = [
        Record(fio="Иванов Иван", composition="Основной", position="Нападающий", titles=5, sport_type="Футбол", rank="Профессионал"),
        Record(fio="Петров Петр", composition="Основной", position="Защитник", titles=3, sport_type="Хоккей", rank="Любитель")
    ]
    XMLWriter.save_to_xml(records, temp_file)
    loaded_records = XMLReader.load_from_xml(temp_file)
    assert len(loaded_records) == 2
    assert loaded_records[0].fio == "Иванов Иван"
    assert loaded_records[1].fio == "Петров Петр"