import unittest
import sys

sys.path.insert(1, '/path/to/geometry_lib/figures')
from figures.figures import Triangle


class TriangleTest(unittest.TestCase):
    def test_triangles(self):
        self.assertEqual(Triangle(1, 2, 3).area, 0)
        self.assertEqual(Triangle(3, 4, 5).area, 6)
        self.assertEqual(Triangle(3.1, 4.1, 5.4).area, 6.317974358922326)

        with self.assertRaises(ValueError):
            Triangle(-1, -2, 3).area
        with self.assertRaises(ValueError):
            Triangle(-12345.6789, 12345, 11111).area
        
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3).area

        with self.assertRaises(TypeError):
            Triangle("test", "test2", "test3").area
        with self.assertRaises(TypeError):
            Triangle(2 + 3j, 2, 4).area


if __name__ == "__main__":
    unittest.main()
