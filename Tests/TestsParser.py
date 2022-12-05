import unittest

from Parser import Parser

class TestsParser(unittest.TestCase):
    def check(self, name, count_number):
        with open(f"C:/Users/German/PycharmProjects/ShikakuPython/Shikakus/{name}.txt") as f:
            shikaku = Parser().parse_puzzle(f.read())
            self.assertEqual(len(shikaku.all_numbers), count_number)

    def test_parse_puzzle1(self):
        self.check("shikaku1", 2)

    def test_parse_puzzle2(self):
        self.check("shikaku2", 3)

    def test_parse_puzzle3(self):
        self.check("shikaku3", 9)

    def test_parse_puzzle4(self):
        self.check("shikaku4", 16)

    def test_parse_puzzle10(self):
        self.check("shikaku10", 34)

