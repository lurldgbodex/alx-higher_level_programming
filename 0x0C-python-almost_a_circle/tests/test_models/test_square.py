#!/usr/bin/python3
"""
Test case for the square class
"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test for square class."""

    def setUp(self):
        self._Base__nb_objects = 0

    def test_attributes(self):
        """Tests for attributes"""
        self.assertEqual(Square(1).id, 1)
        s = Square(5, 3, 4)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.id, 2)

    def test_str_rep(self):
        """Test for __str__ representation"""
        s1 = Square(9, 4, 5, 6)
        self.assertEqual(str(s1), "[Square] (6) 4/5 - 9")

    def test_super(self):
        """Test for inheritance"""
        s = Square(6)
        self.assertTrue(isinstance(s, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(s, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

        s1 = Square(9)
        self.assertEqual(s1.area(), 81)
        s2 = Square(4, 1, 2, 5)
        s2.update(7)
        self.assertEqual(s2.id, 7)
        f = io.StringIO()
        s3 = Square(4)
        with contextlib.redirect_stdout(f):
            s3.display()
        s = f.getvalue()
        res = "####\n####\n####\n####\n"
        self.assertEqual(s, res)

    def test_args(self):
        """Test for missing args"""
        with self.assertRaises(TypeError) as e:
            Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'", str(
                e.exception))

    def test_for_some_attributes(self):
        """Test for square attributes"""
        s1 = Square(8)
        self.assertEqual(s1.size, 8)
        s2 = Square(9, 8, 7, 2)
        self.assertEqual(s2.size, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("Hello", 2)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "World")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "Foo", 3)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)

        with self.assertRaisesRegex(ValueError, "width must be >0"):
            Square(-1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -3)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 5, -5, 6)

    def test_update(self):
        """Test update method on square class"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(x=12)
        self.assertEqual(s1.x, 12)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)
        s1.update()
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)
        s1 = Square(9)
        with self.assertRaises(TypeError) as x:
            s1.update(2, 3, 4, "hello")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s1.update("hello", 8, 9)
        self.assertEqual("id must be an integer", str(x.exception))

    def test_to_dictionary(self):
        """Test the to_dictionary on square class"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s_dictionary = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(len(s1_dictionary), len(s_dictionary))
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(len(s1_dictionary), len(s2_dictionary))
        self.assertEqual(type(s2_dictionary), dict)
        self.assertFalse(s1 == s2)

        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            s1 = Square(10, 2, 1, 9)
            s1.to_dictionary("Hi")
        self.assertEqual(s, str(x.exception))


if __name__ == '__main__':
    unittest.main()
