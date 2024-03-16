"""Unittest for max_integer([..])
"""
from unittest import TestCase
max_int = __import__('6-max_integer').max_integer


class TestMax(TestCase):
    """
    test max function
    """
    def test_type(self):
        self.assertRaises(TypeError, max_int, ["a", "b"])
        self.assertRaises(TypeError, max_int, [2.3, 3.0])
        self.assertRaises(TypeError, max_int, [1, "a", 3])

    def test_max(self):
        # Test case where all integers are positive
        self.assertEqual(max_int([1, 3, 2]), 3)

        # Test case where all integers are negative
        self.assertEqual(max_int([-1, -3, -2]), -1)

        # Test case where list contains positive and negative integers
        self.assertEqual(max_int([-1, 3, -2]), 3)

        # Test case where list contains only one integer
        self.assertEqual(max_int([7]), 7)

    def test_empty_list(self):
        # Test case where list is empty
        self.assertIsNone(max_int([]))

