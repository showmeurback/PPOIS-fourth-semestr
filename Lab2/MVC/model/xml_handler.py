import xml.dom.minidom as dom
import xml.sax
from MVC.model.record import Record

class XMLWriter:
    @staticmethod
    def save_to_xml(records, file_path):
        """
        Сохраняет массив записей в XML-файл с использованием DOM парсера.
        """
        doc = dom.Document()
        root = doc.createElement("records")
        doc.appendChild(root)

        for record in records:
            record_element = doc.createElement("record")

            fio_element = doc.createElement("fio")
            fio_element.appendChild(doc.createTextNode(record.fio))
            record_element.appendChild(fio_element)

            composition_element = doc.createElement("composition")
            composition_element.appendChild(doc.createTextNode(record.composition))
            record_element.appendChild(composition_element)

            position_element = doc.createElement("position")
            position_element.appendChild(doc.createTextNode(record.position))
            record_element.appendChild(position_element)

            titles_element = doc.createElement("titles")
            titles_element.appendChild(doc.createTextNode(str(record.titles)))
            record_element.appendChild(titles_element)

            sport_type_element = doc.createElement("sport_type")
            sport_type_element.appendChild(doc.createTextNode(record.sport_type))
            record_element.appendChild(sport_type_element)

            rank_element = doc.createElement("rank")
            rank_element.appendChild(doc.createTextNode(record.rank))
            record_element.appendChild(rank_element)

            root.appendChild(record_element)

        with open(file_path, "w", encoding="utf-8") as file:
            doc.writexml(file, indent="\t", newl="\n", encoding="utf-8")


class XMLReader(xml.sax.ContentHandler):
    """
    Читает данные из XML-файла с использованием SAX парсера.
    """
    def __init__(self):
        self.records = []
        self.current_data = None
        self.current_record = None

    def startElement(self, tag, attributes):
        if tag == "record":
            self.current_record = Record("", "", "", 0, "", "")
        elif self.current_record:
            self.current_data = tag

    def endElement(self, tag):
        if tag == "record" and self.current_record:
            self.records.append(self.current_record)
            self.current_record = None

    def characters(self, content):
        if self.current_data and self.current_record:
            if self.current_data == "fio":
                self.current_record.fio = content
            elif self.current_data == "composition":
                self.current_record.composition = content
            elif self.current_data == "position":
                self.current_record.position = content
            elif self.current_data == "titles":
                self.current_record.titles = int(content)
            elif self.current_data == "sport_type":
                self.current_record.sport_type = content
            elif self.current_data == "rank":
                self.current_record.rank = content
            self.current_data = None

    @staticmethod
    def load_from_xml(file_path):
        handler = XMLReader()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(file_path)
        return handler.records