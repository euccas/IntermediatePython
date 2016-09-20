import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Point of {} and {} and {}".format(self.x, self.y, self.z)

    def __repr__(self):
        return "Point(x={}, y={}, z={})".format(self.x, self.y, self.z)

    def distance(self, point):
        # Pythagorean Theorem
        x = self.x - point.x
        y = self.y - point.y
        z = self.z - point.z
        return math.sqrt(x**2 + y**2 + z**2)

    def shift(self, point):
        return Point(self.x + point.x, self.y + point.y, self.z + point.z)

    def scale(self, num):
        return Point(num * self.x, num * self.y, num * self.z)