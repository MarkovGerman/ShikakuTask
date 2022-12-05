import unittest
from Coordinates import Coordinates
from Rectangle import Rectangle

class TestsRectangle(unittest.TestCase):
    def test_is_cross(self):
        rect1 = Rectangle(Coordinates(1,1), Coordinates(1,1))
        rect2 = Rectangle(Coordinates(2,2), Coordinates(2,2))
        self.assertEqual(rect1.is_cross(rect2), False)

    def test_is_cross_easy(self):
        rect1 = Rectangle(Coordinates(1, 1), Coordinates(1, 5))
        rect2 = Rectangle(Coordinates(1, 1), Coordinates(1, 1))
        self.assertEqual(rect1.is_cross(rect2), True)

    def test_is_cross_easy2(self):
        rect1 = Rectangle(Coordinates(4,4), Coordinates(4,4))
        rect2 = Rectangle(Coordinates(4, 0), Coordinates(4,3))
        self.assertEqual(rect1.is_cross(rect2), False)


