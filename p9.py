"""Point(x, y) stores both coordinates
__add__ returns a new Point with the sums
__eq__ compares x and y
__str__ returns "(4, 6)"
Add Point(1, 2) + Point(3, 4), print it, then compare"""
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"({self.x},{self.y})"

p = Point(1, 2) + Point(3, 4)
print(p)
print(p == Point(4, 6), p == Point(0, 0))