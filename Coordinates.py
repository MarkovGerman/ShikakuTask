class Coordinates:
    """Класс координат"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def is_inside(self, coor1, coor2):
        return max(coor1.x, coor2.x) >= self.x >= min(coor1.x, coor2.x) \
               and max(coor1.y, coor2.y) >= self.y >= min(coor1.y, coor2.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinates(self.x - other.x, self.y - other.y)
