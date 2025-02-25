import unittest
from Source.runway import Runway

class TestRunway(unittest.TestCase):
    def setUp(self):
        self.runway = Runway()

    def test_initial_state(self):
        self.assertTrue(self.runway.is_available)

    def test_occupy_runway(self):
        self.runway.occupy()
        self.assertFalse(self.runway.is_available)

    def test_free_runway(self):
        self.runway.occupy()
        self.runway.free()
        self.assertTrue(self.runway.is_available)

    def test_double_occupy(self):
        self.runway.occupy()
        self.runway.occupy()  # Попытка занять уже занятую полосу
        self.assertFalse(self.runway.is_available)

    def test_double_free(self):
        self.runway.free()
        self.runway.free()  # Попытка освободить уже свободную полосу
        self.assertTrue(self.runway.is_available)

if __name__ == "__main__":
    unittest.main()