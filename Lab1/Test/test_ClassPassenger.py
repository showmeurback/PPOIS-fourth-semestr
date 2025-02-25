import unittest
from Source.passenger import Passenger
from Source.ticket import Ticket

class TestPassenger(unittest.TestCase):
    def setUp(self):
        self.ticket = Ticket(flight_number="FL123", seat="A1")
        self.passenger = Passenger(name="John Doe", ticket=self.ticket)

    def test_init(self):
        self.assertEqual(self.passenger.name, "John Doe")
        self.assertEqual(self.passenger.ticket.flight_number, "FL123")
        self.assertEqual(self.passenger.ticket.seat, "A1")

    def test_name_property(self):
        self.assertEqual(self.passenger.name, "John Doe")
        self.passenger.name = "Jane Doe"
        self.assertEqual(self.passenger.name, "Jane Doe")

    def test_ticket_property(self):
        self.assertIsInstance(self.passenger.ticket, Ticket)
        new_ticket = Ticket(flight_number="FL456", seat="B2")
        self.passenger.ticket = new_ticket
        self.assertEqual(self.passenger.ticket.flight_number, "FL456")
        self.assertEqual(self.passenger.ticket.seat, "B2")

    def test_string_representation(self):
        # Проверяем, что строковое представление объекта существует
        self.assertTrue(str(self.passenger).startswith("<Source.passenger.Passenger object at"))

if __name__ == "__main__":
    unittest.main()