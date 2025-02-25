import unittest
from unittest.mock import patch
from io import StringIO
from Source.inflight_service import InflightService

class TestInflightService(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        # Создаем экземпляр класса InflightService
        self.inflight_service = InflightService()

    def test_serve_meal(self):
        """Test serving meals to passengers."""
        # Перехватываем вывод в консоль
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.inflight_service.serve_meal()
            output = fake_output.getvalue().strip()  # Получаем содержимое вывода

        # Проверяем, что сообщение о подаче еды корректно
        expected_output = "Serving meals to passengers."
        self.assertEqual(output, expected_output)

    def test_serve_drinks(self):
        """Test serving drinks to passengers."""
        # Перехватываем вывод в консоль
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.inflight_service.serve_drinks()
            output = fake_output.getvalue().strip()  # Получаем содержимое вывода

        # Проверяем, что сообщение о подаче напитков корректно
        expected_output = "Serving drinks to passengers."
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()