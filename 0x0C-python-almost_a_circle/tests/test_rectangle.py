import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_zero_width_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 5)

        with self.assertRaises(ValueError):
            r = Rectangle(5, 0)

    def test_negative_width_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10)

        with self.assertRaises(ValueError):
            r = Rectangle(10, -5)

    def test_non_numeric_width_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle("width", 10)

        with self.assertRaises(TypeError):
            r = Rectangle(10, "height")

    def test_non_numeric_x_y(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, "x", 0)

        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, 0, "y")

    def test_large_width_height(self):
        r = Rectangle(2**31, 2**31)  # Testing with large values
        self.assertEqual(r.width, 2**31)
        self.assertEqual(r.height, 2**31)

    def test_all_attributes_same_value(self):
        r = Rectangle(5, 5, 5, 5)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)

    def test_boundary_values(self):
        r = Rectangle(2**31 - 1, 2**31 - 1, 2**31 - 1, 2**31 - 1)  # Testing with maximum integer values
        self.assertEqual(r.width, 2**31 - 1)
        self.assertEqual(r.height, 2**31 - 1)
        self.assertEqual(r.x, 2**31 - 1)
        self.assertEqual(r.y, 2**31 - 1)

    def test_negative_x_y(self):
        with self.assertRaises(ValueError):
            r = Rectangle(20, 30, -2, -3, 1)

    def test_negative_or_zero_width_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-20, 30, 2, 3, 1)

        with self.assertRaises(ValueError):
            r = Rectangle(20, -30, 2, 3, 1)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 30, 2, 3, 1)

        with self.assertRaises(ValueError):
            r = Rectangle(20, 0, 2, 3, 1)
