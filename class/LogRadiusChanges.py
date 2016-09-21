# Modify the Circle class we defined previously to use a property for the radius and record changes to the radius in a radius_changes attribute.
#
# Hint
#
# You will need to store the actual radius somewhere. You may want to use a _radius attribute when converting the radius to a property.
#
# Example usage:
#
# >>> circle = Circle()
# >>> circle.radius
# 1
# >>> circle.radius_changes
# [1]
# >>> circle.radius = 2
# >>> circle.radius = 3
# >>> circle.radius_changes
# [1, 2, 3]
#
# Take our Circle class and modify it again to raise a ValueError when the radius or diameter are set to a negative number.

import math

class Circle:
    def __init__(self, radius=1):
        self._radius = radius
        self.radius_changes = [radius]

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius
        self.radius_changes.append(self._radius)
