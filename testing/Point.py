import unittest
from point import Point

class PointTests(unittest.TestCase):
    def test_values(self):
        p = Point(x=1, y=2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_iteration(self):
        p = Point(x=1, y=2)
        x, y = p
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)

if __name__ == "__main__":
    unittest.main()