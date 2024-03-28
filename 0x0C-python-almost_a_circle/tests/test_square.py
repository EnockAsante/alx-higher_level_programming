import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_initialization(self):
        s = Square(5)
        self.assertEqual(s.id, 17)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_initialization_with_id(self):
        s = Square(5, id=1)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_initialization_with_coordinates(self):
        s = Square(5, x=2, y=3)
        self.assertEqual(s.id, 18)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_str_representation(self):
        s = Square(5, x=2, y=3, id=1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")

    def test_update_with_args(self):
        s = Square(5)
        s.update(1, 10, 20, 30)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 30)

    def test_update_with_kwargs(self):
        s = Square(5)
        s.update(id=1, size=10, x=20, y=30)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 30)

    def test_to_dictionary(self):
        s = Square(5, x=2, y=3, id=1)
        expected_dict = {'id': 1, 'x': 2, 'y': 3, 'size': 5}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_negative(self):
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -10

    def test_size_setter_non_integer(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "abc"
