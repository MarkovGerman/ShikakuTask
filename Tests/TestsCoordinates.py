import unittest

from Coordinates import Coordinates

class TestsCoordinates(unittest.TestCase):
    def test_check_eq(self):
        self.assertEqual(Coordinates(1,4) == Coordinates(4,1), False)
        self.assertEqual(Coordinates(2,2) == Coordinates(3,3), False)
        self.assertEqual(Coordinates(1,5) == Coordinates(1,5), True)

    def test_check_hash(self):
        coordinates = [Coordinates(1,1), Coordinates(4,4), Coordinates(3,2), Coordinates(7,9)]
        for c in coordinates:
            self.assertEqual(hash(c), hash((c.x, c.y)))

    def test_check_add(self):
        self.assertEqual(Coordinates(1,1) + Coordinates(2,4), Coordinates(3,5))
        self.assertEqual(Coordinates(1,3) + Coordinates(-7, 8), Coordinates(-6, 11))
        self.assertEqual(Coordinates(5,6) + Coordinates(5, 4), Coordinates(10, 10))

    def test_sub(self):
        self.assertEqual(Coordinates(2,2) - Coordinates(1,0), Coordinates(1,2))
        self.assertEqual(Coordinates(5,4) - Coordinates(2,3), Coordinates(3,1))
        self.assertEqual(Coordinates(10,10) - Coordinates(11, 12), Coordinates(-1,-2))
