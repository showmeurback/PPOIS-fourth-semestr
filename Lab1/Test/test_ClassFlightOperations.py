import unittest
from unittest.mock import patch
from io import StringIO
from Source.flight_operations import FlightOperations

class TestFlightOperations(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.flight_operations = FlightOperations()

    def test_plan_route_valid(self):
        """Test planning a valid route."""
        start = "Moscow"
        destination = "London"

        # Перехватываем вывод в консоль
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.flight_operations.plan_route(start=start, destination=destination)
            output = fake_output.getvalue().strip()  # Получаем содержимое вывода

        # Проверяем, что маршрут был успешно запланирован (учитываем точку в конце)
        expected_output = f"Route planned: {start} -> {destination}."
        self.assertEqual(output, expected_output)

    def test_plan_route_empty_start(self):
        """Test planning a route with an empty starting location."""
        start = ""
        destination = "London"

        # Перехватываем вывод в консоль
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.flight_operations.plan_route(start=start, destination=destination)
            output = fake_output.getvalue().strip()  # Получаем содержимое вывода

        # Проверяем, что маршрут был запланирован с пустым начальным пунктом (учитываем точку в конце)
        expected_output = f"Route planned:  -> {destination}."
        self.assertEqual(output, expected_output)

    def test_plan_route_empty_destination(self):
        """Test planning a route with an empty destination."""
        start = "Moscow"
        destination = ""

        # Перехватываем вывод в консоль
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.flight_operations.plan_route(start=start, destination=destination)
            output = fake_output.getvalue().strip()  # Получаем содержимое вывода

        # Проверяем, что маршрут был запланирован с пустым пунктом назначения (учитываем точку в конце)
        expected_output = f"Route planned: {start} -> ."
        self.assertEqual(output, expected_output)

    def test_ensure_safety(self):
        """Test ensuring safety procedures."""
        # Перехватываем вывод в консоль
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.flight_operations.ensure_safety()
            output = fake_output.getvalue().strip()  # Получаем содержимое вывода

        # Проверяем, что процедуры безопасности выполнены успешно (учитываем точку в конце)
        expected_output = "Safety procedures completed."
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()