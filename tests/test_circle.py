import unittest
from math import pi
import sys

sys.path.insert(1, '/path/to/geometry_lib/figures')
from figures import Circle


class CircleTest(unittest.TestCase):
    def test_circles(self):
        self.assertEqual(Circle(1).area, pi)
        self.assertEqual(Circle(0).area, 0)
        self.assertEqual(Circle(3).area, pi * 3 ** 2)
        self.assertEqual(Circle(2.34).area, pi * 2.34 ** 2)

        with self.assertRaises(ValueError):
            Circle(-1).area
        with self.assertRaises(ValueError):
            Circle(-12345.6789).area
        
        with self.assertRaises(TypeError):
            Circle("test").area
        with self.assertRaises(TypeError):
            Circle(2 + 3j).area


if __name__ == "__main__":
    unittest.main()
