import unittest
from Source.airplane import Airplane
from Source.passenger import Passenger
from Source.crew import Crew
from Source.ticket import Ticket

class TestAirplane(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        # Create an airplane instance with a capacity of 400 passengers
        self.airplane = Airplane(model="Boeing 747", capacity=400)

        # Create tickets for testing
        self.ticket1 = Ticket(flight_number="FL123", seat="A1")
        self.ticket2 = Ticket(flight_number="FL123", seat="B2")

        # Create passengers for testing
        self.passenger1 = Passenger(name="Ivan Ivanov", ticket=self.ticket1)
        self.passenger2 = Passenger(name="Petr Petrov", ticket=self.ticket2)

        # Create crew members for testing
        self.crew1 = Crew(name="Alexander Sidarov", role="Pilot")
        self.crew2 = Crew(name="Maria Ivanova", role="Flight Attendant")

    def test_add_passenger(self):
        """Test the add_passenger method."""
        # Add a passenger to the airplane
        self.airplane.add_passenger(self.passenger1)
        self.assertIn(self.passenger1, self.airplane.passengers)  # Ensure the passenger is added

        # Check that the airplane does not accept more passengers than its capacity
        for _ in range(400):
            self.airplane.add_passenger(Passenger(name="Test Passenger", ticket=Ticket(flight_number="FL123", seat="C1")))
        self.assertEqual(len(self.airplane.passengers), 400)  # Capacity limit reached
        self.airplane.add_passenger(self.passenger2)  # Attempt to add another passenger
        self.assertNotIn(self.passenger2, self.airplane.passengers)  # Ensure the passenger was not added

    def test_add_crew(self):
        """Test the add_crew method."""
        # Add a crew member to the airplane
        self.airplane.add_crew(self.crew1)
        self.assertIn(self.crew1, self.airplane.crew)  # Ensure the crew member is added

        # Add another crew member to the airplane
        self.airplane.add_crew(self.crew2)
        self.assertIn(self.crew2, self.airplane.crew)  # Ensure the second crew member is added

    def test_take_off(self):
        """Test the take_off method."""
        # Check the initial status of the airplane
        self.assertEqual(self.airplane.status, "on_ground")

        # Perform a takeoff
        self.airplane.take_off()
        self.assertEqual(self.airplane.status, "in_air")  # Ensure the airplane is now in the air

        # Check that the airplane cannot take off again while already in the air
        self.airplane.take_off()
        self.assertEqual(self.airplane.status, "in_air")  # Status remains "in_air"

    def test_land(self):
        """Test the land method."""
        # Check the initial status of the airplane
        self.assertEqual(self.airplane.status, "on_ground")

        # Perform a takeoff
        self.airplane.take_off()
        self.assertEqual(self.airplane.status, "in_air")  # Ensure the airplane is now in the air

        # Perform a landing
        self.airplane.land()
        self.assertEqual(self.airplane.status, "on_ground")  # Ensure the airplane is now on the ground

        # Check that the airplane cannot land again while already on the ground
        self.airplane.land()
        self.assertEqual(self.airplane.status, "on_ground")  # Status remains "on_ground"

    def test_capacity_limit(self):
        """Test the capacity limit of the airplane."""
        # Fill the airplane to its full capacity
        for i in range(400):
            ticket = Ticket(flight_number="FL123", seat=f"C{i + 1}")
            passenger = Passenger(name=f"Passenger {i + 1}", ticket=ticket)
            self.airplane.add_passenger(passenger)

        # Check that no additional passengers can be added beyond the capacity
        ticket = Ticket(flight_number="FL123", seat="Z1")
        extra_passenger = Passenger(name="Extra Passenger", ticket=ticket)
        self.airplane.add_passenger(extra_passenger)
        self.assertNotIn(extra_passenger, self.airplane.passengers)  # Ensure the extra passenger was not added

if __name__ == "__main__":
    unittest.main()