import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_initialization_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, None)
        self.assertEqual(obj2.id, None)

    def test_initialization_with_id(self):
        obj = Base(id = 100)
        self.assertEqual(obj.id, 100)

    def test_id_passed_as_argument(self):
        obj = Base(id = 10)
        self.assertEqual(obj.id, 10)

    def test_zero_id(self):
        obj = Base(id = 0)
        self.assertEqual(obj.id, 0)

    def test_large_id(self):
        obj = Base(id = 10 ** 18)
        self.assertEqual(obj.id, 10 ** 18)
