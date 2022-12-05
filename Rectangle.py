from Coordinates import Coordinates


class Rectangle:
    def __init__(self, lower_left=Coordinates(-1,-1), upper_right=Coordinates(-1,-1), number=0, color=None):
        self.lower_left:Coordinates = Coordinates(min(lower_left.x, upper_right.x), min(lower_left.y, upper_right.y))
        self.upper_right:Coordinates = Coordinates(max(lower_left.x, upper_right.x), max(lower_left.y, upper_right.y))
        self.color = color
        self.number = number

    def is_cross(self, other):
        return not (self.upper_right.x < other.lower_left.x or self.upper_right.y < other.lower_left.y
                    or self.lower_left.y > other.upper_right.y or self.lower_left.x > other.upper_right.x)

    def __eq__(self, other):
        return self.lower_left == other.lower_left and self.upper_right == other.upper_right




