from Cell import Cell
from colorama import Back
from Rectangle import Rectangle
from Coordinates import Coordinates

Colors = [Back.BLUE, Back.GREEN, Back.BLACK, Back.CYAN, Back.RED, Back.YELLOW, Back.WHITE, Back.LIGHTBLACK_EX,
          Back.LIGHTBLUE_EX, Back.LIGHTGREEN_EX]


class Shikaku:
    def __init__(self, size):
        self.size = size
        self.cells: list[list[Cell]] = []
        self.rectangles: list[Rectangle] = []
        self.all_numbers: list[Cell] = []

        for x in range(self.size):
            row = []
            for y in range(self.size):
                cell = Cell(x,y)
                row.append(cell)
            self.cells.append(row)

    @property
    def counter(self):
        return len(self.rectangles)

    @property
    def is_solve(self):
        return len(self.all_numbers) == len(self.rectangles)

    def __copy__(self):
        copy = Shikaku(self.size)
        copy.all_numbers = [e for e in self.all_numbers]
        copy.rectangles = [e for e in self.rectangles]
        return copy

    def __eq__(self, other):
        return self.rectangles != other.rectangles

    def __str__(self):
        string = ""
        l = 3
        for row in self.cells:
            for cell in row:
                string += str(cell) + ' ' * (l - len(str(cell.number)))
            string += Back.RESET + '\n'
        return string

    def add_number(self, coordinates, number):
        x, y = coordinates.x, coordinates.y
        cell = Cell(coordinates.x, coordinates.y, number)
        self.all_numbers.append(cell)
        self.cells[x][y] = Cell(x,y, number, Colors[self.counter % len(Colors)], True)

    def add_rectangle(self, cell: Cell, rectangle:Rectangle):
        copy = self.__copy__()
        copy.rectangles.append(rectangle)
        return copy

    def check_rect_indexes(self, rect:Rectangle):
        return self.size > rect.upper_right.x and self.size > rect.upper_right.y \
               and rect.lower_left.x >= 0 and rect.lower_left.y >= 0

    def check_rect_numbers(self, rect:Rectangle, cell:Cell):
        if not self.check_rect_indexes(rect):
            return False
        for number in self.all_numbers:
            if number.coordinates != cell.coordinates and Rectangle(Coordinates(number.x, number.y), Coordinates(number.x, number.y)).is_cross(rect):
                return False
        for rectangle in self.rectangles:
            if rectangle.is_cross(rect):
                return False
        return True

    def colorize(self):
        index = 0
        for rect in self.rectangles:
            for i in range(rect.lower_left.x, rect.upper_right.x + 1):
                for j in range(rect.lower_left.y, rect.upper_right.y + 1):
                    self.cells[i][j].color = Colors[index % len(Colors)]
                    self.cells[i][j].number = rect.number
            index += 1
