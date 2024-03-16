"""Unittest for max_integer([..])
"""
from unittest import TestCase

max_int = __import__('6-max_integer').max_integer


class TestMax(TestCase):
    """
    test max function
    """

    def test_type(self):
        self.assertRaises(TypeError, max_int, ["h", 1])
        self.assertRaises(TypeError, max_int, [2, [2, 1]])

    def test_max(self):
        # Test case where all integers are positive
        self.assertEqual(max_int([1, 3, 2]), 3)

        # Test case where all integers are negative
        self.assertEqual(max_int([-1, -3, -2]), -1)

        # Test case where list contains positive and negative integers
        self.assertEqual(max_int([-1, 3, -2]), 3)

        # Test case where list contains only one integer
        self.assertEqual(max_int([7]), 7)
        self.assertEqual(max_int([]), None)
        self.assertEqual(max_int([]), None)
        self.assertEqual(max_int([3]), 3)
        self.assertEqual(max_int([-3]), -3)
        self.assertEqual(max_int([-1, -2, -3]), -1)
        self.assertEqual(max_int([15, 10, 5]), 15)
        self.assertEqual(max_int([15, 10, 5, -5, -10, 15]), 15)
        self.assertEqual(max_int([15, 15, 15]), 15)

