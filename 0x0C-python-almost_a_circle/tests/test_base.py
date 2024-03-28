import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_initialization_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_initialization_with_id(self):
        obj = Base(id=100)
        self.assertEqual(obj.id, 100)

    def test_id_passed_as_argument(self):
        obj = Base(id=10)
        self.assertEqual(obj.id, 10)

    def test_zero_id(self):
        obj = Base(id=0)
        self.assertEqual(obj.id, 5)

    def test_large_id(self):
        obj = Base(id=10 ** 18)
        self.assertEqual(obj.id, 10 ** 18)

    def test_multiple_instances(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base(id=10)
        obj4 = Base(id=20)
        self.assertEqual(obj1.id, 3)
        self.assertEqual(obj2.id, 4)
        self.assertEqual(obj3.id, 10)
        self.assertEqual(obj4.id, 20)

    def test_max_id(self):
        obj = Base(id=(2 ** 31) - 1)
        self.assertEqual(obj.id, (2 ** 31) - 1)
