from Shikaku import Shikaku
from Coordinates import Coordinates


class Parser:
    def __init__(self, string=None):
        self.string = string
        self.size = 0
        self.puzzle = None

    def parse_puzzle(self, string):
        self.string = string
        rows = self.string.split('\n')
        self.size = int(rows[0])
        self.puzzle = Shikaku(self.size)
        for x in range(1, len(rows)):
            elements = rows[x].split()
            if len(elements) != self.size:
                raise ValueError(f"Неправильно введена строка {str(x-1)}")
            for y in range(len(elements)):
                cell = elements[y]
                if not cell == "0":
                    self.puzzle.add_number(Coordinates(x-1, y), int(cell))
        return self.puzzle
