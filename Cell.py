from colorama import Back
from Coordinates import Coordinates


class Cell:
    """Класс для ячейки поля"""
    def __init__(self,  x, y, number=0, color=None, is_busy=False):
        self.color = color
        self.x = x
        self.y = y
        self.coordinates = Coordinates(x,y)
        self.number = number
        self.is_busy = is_busy

    @property
    def divisors(self):
        return self.get_all_divisors()

    def __str__(self):
        if self.color is None:
            return str(self.number)
        else:
            return self.color + str(self.number)

    def get_all_divisors(self):
        dividers = []
        n = self.number
        for i in range(1, int(n / 2) + 1):
            if n % i == 0:
                dividers.append(i)
        dividers.append(n)
        return dividers
