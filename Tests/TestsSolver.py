import unittest

from Solver import Solver
from Coordinates import Coordinates
from Cell import Cell
from Rectangle import Rectangle
from Parser import Parser

class TestsSolver(unittest.TestCase):
    def test(self):
        with open("C:/Users/German/PycharmProjects/ShikakuPython/Shikakus/shikaku3.txt") as f:
            shikaku = Parser().parse_puzzle(f.read())
            cell = Cell(4, 4, 4)
            self.assertEqual(Solver.find_all_rectangles(shikaku, cell)[0], Rectangle(Coordinates(1,4), Coordinates(4,4)))

    def test_easy(self):
        with open("C:/Users/German/PycharmProjects/ShikakuPython/Shikakus/shikaku3.txt") as f:
            shikaku = Parser().parse_puzzle(f.read())
            cell = Cell(4, 3, 4)
            self.assertEqual(Solver.find_all_rectangles(shikaku, cell)[0], Rectangle(Coordinates(4,0), Coordinates(4,3)))

    def test_medium(self):
        with open("C:/Users/German/PycharmProjects/ShikakuPython/Shikakus/shikaku5.txt") as f:
            shikaku = Parser().parse_puzzle(f.read())
            cell = Cell(6,0, 4)
            self.assertEqual(len(Solver.find_all_rectangles(shikaku, cell)), 2)

    def test_solve(self):
        with open("C:/Users/German/PycharmProjects/ShikakuPython/Shikakus/shikaku1.txt") as f:
            shikaku = Parser().parse_puzzle(f.read())
            result = Solver.solve(shikaku)
            self.assertEqual(len(result), 2)
