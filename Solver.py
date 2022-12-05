from queue import Queue
from Shikaku import Shikaku
from collections import defaultdict

from colorama import Back
from Cell import Cell
from Rectangle import Rectangle
from Coordinates import Coordinates


class Solver:
    @staticmethod
    def solve(puzzle: Shikaku):
        result = []
        puzzle.all_numbers.sort(key=lambda x: x.number, reverse=True)
        if not Solver.check_possible_solve(puzzle):
            raise ValueError("Неправильно введена головоломка")
        queue: [Shikaku] = [puzzle]
        while queue:
            task = queue.pop(0)
            if task.is_solve:
                task.colorize()
                result.append(task)
            else:
                cell = task.all_numbers[task.counter]
                rects = Solver.find_all_rectangles(task, cell)
                for rect in rects:
                    queue.append(task.add_rectangle(cell, rect))
        return result

    @staticmethod
    def find_all_rectangles(puzzle: Shikaku, cell: Cell):
        #Получаем все прямоугольники для одной клетки
        rectangles = []
        #cell = puzzle.cells[cell.x][cell.y]
        dividers = cell.divisors
        for i in range(len(cell.divisors)):
            width = dividers[i]
            height = dividers[len(dividers) - i - 1]
            for w in range(width):
                for h in range(height):
                    left = cell.coordinates - Coordinates(w, h)
                    right = cell.coordinates + Coordinates(width - 1 - w, height - 1 - h)
                    upper_right = Coordinates(max(left.x, right.x), max(left.y, right.y))
                    lower_left = Coordinates(min(left.x, right.x), min(left.y, right.y))
                    rect = Rectangle(lower_left, upper_right, cell.number)
                    if puzzle.check_rect_numbers(rect, cell):
                        rectangles.append(rect)
        return rectangles

    @staticmethod
    def check_possible_solve(puzzle: Shikaku):
        return sum([e.number for e in puzzle.all_numbers]) == puzzle.size * puzzle.size
