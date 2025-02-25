import unittest
from Source.ticket import Ticket

class TestTicket(unittest.TestCase):
    def setUp(self):
        self.ticket = Ticket(flight_number="FL123", seat="A1")

    def test_init(self):
        self.assertEqual(self.ticket.flight_number, "FL123")
        self.assertEqual(self.ticket.seat, "A1")

    def test_flight_number_property(self):
        self.assertEqual(self.ticket.flight_number, "FL123")
        self.ticket.flight_number = "FL456"
        self.assertEqual(self.ticket.flight_number, "FL456")

    def test_seat_property(self):
        self.assertEqual(self.ticket.seat, "A1")
        self.ticket.seat = "B2"
        self.assertEqual(self.ticket.seat, "B2")


if __name__ == "__main__":
    unittest.main()