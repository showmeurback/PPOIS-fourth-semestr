import unittest
from Source.crew import Crew

class TestCrew(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        # Создаем экземпляр класса Crew
        self.crew_member = Crew(name="John Doe", role="Pilot")

    def test_init(self):
        """Test the initialization of the Crew object."""
        # Проверяем, что атрибуты правильно установлены при создании объекта
        self.assertEqual(self.crew_member.name, "John Doe", "Name should be 'John Doe'")
        self.assertEqual(self.crew_member.role, "Pilot", "Role should be 'Pilot'")

    def test_name_and_role(self):
        """Test the name and role attributes."""
        # Проверяем доступ к атрибутам name и role
        self.assertEqual(self.crew_member.name, "John Doe", "Name should be accessible via the name attribute")
        self.assertEqual(self.crew_member.role, "Pilot", "Role should be accessible via the role attribute")

        # Изменяем атрибуты напрямую (если это допустимо в текущей реализации)
        self.crew_member.name = "Jane Doe"
        self.crew_member.role = "Co-pilot"
        self.assertEqual(self.crew_member.name, "Jane Doe", "Name should be updated to 'Jane Doe'")
        self.assertEqual(self.crew_member.role, "Co-pilot", "Role should be updated to 'Co-pilot'")

    def test_string_representation(self):
        """Test the existence of the Crew object."""
        # Проверяем, что объект успешно создан
        self.assertIsNotNone(self.crew_member, "Crew member should not be None")

        # Проверяем, что атрибуты name и role доступны
        self.assertEqual(self.crew_member.name, "John Doe", "Name should be 'John Doe'")
        self.assertEqual(self.crew_member.role, "Pilot", "Role should be 'Pilot'")

    def test_equality(self):
        """Test equality of two Crew objects."""
        # Создаем два одинаковых объекта
        crew1 = Crew(name="John Doe", role="Pilot")
        crew2 = Crew(name="John Doe", role="Pilot")

        # Так как метод __eq__ не определен, сравниваем по ссылкам
        self.assertIsNot(crew1, crew2, "Two identical crew members should not be the same object")

        # Создаем разные объекты
        crew3 = Crew(name="Jane Doe", role="Flight Attendant")
        self.assertNotEqual(crew1, crew3, "Different crew members should not be equal")

if __name__ == "__main__":
    unittest.main()