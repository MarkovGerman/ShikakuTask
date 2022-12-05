import unittest
from colorama import Back
from Cell import Cell

class TestsCell(unittest.TestCase):
    def test_divisors_easy_number(self):
        cell = Cell(0, 0, 4)
        self.assertEqual(cell.divisors, [1,2,4])

    def test_divisors_medium_number(self):
        cell = Cell(0, 0, 12)
        self.assertEqual(cell.divisors, [1,2,3,4,6,12])

    def test_divisors_hard(self):
        self.assertEqual(Cell(0,0,100).divisors, [1, 2, 4, 5, 10, 20, 25, 50, 100])

    def test_str(self):
        self.assertEqual(str(Cell(1,1,10)), "10")

    def test_str2(self):
        self.assertEqual(str(Cell(0, 0, 12, color=Back.BLACK)), Back.BLACK + "12")