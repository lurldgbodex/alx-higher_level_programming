#!/usr/bin/python3
"""
Unittest rectangle
Test cases for the Rectangle class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import contextlib


class TestRectangle(unittest.TestCase):
    """Test cases for the rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_for_id(self):
        """Test for task 2"""
        r1 = Rectangle(10, 2)
        self.assertTrue(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertTrue(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertTrue(r3.id, 12)
        r4 = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(r4.id, -5)

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_more_than_5_args(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 7, 9, 2, 1, 8)

    def test_one_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_width_integer(self):
        """Test if width is an integer"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_height_integer(self):
        """Test if height is a type(int)"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "10")

    def test_x_integer(self):
        """Test if x is of type(int)"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3", 4)

    def test_y_integer(self):
        """Tests if y is of type(int)"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_width_valid(self):    
        """Test if width is a valid value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 1)
    
    def test_height_valid(self):
        """Test if height is a valid value"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
    
    def test_x_valid(self):
        """Test if x is a valid value"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 1, -1, 8)
    
    def test_y_valid(self):
        """Test if y is a valid value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(5, 3, 8, -12)

    def test_area(self):
        """Test the public method area"""
        self.assertEqual(Rectangle(10, 2).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
        with self.assertRaises(TypeError) as e:
            r = Rectangle(3, 2)
            r.area("6")
        self.assertEqual("area() takes 1 positional argument but 2 were given", str(e.exception))

    def test_display(self):
        """Test the display method of rectangle"""
        f = io.StringIO()
        r1 = Rectangle(4, 5)
        with contextlib.redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        res = "####\n####\n####\n####\n####\n"
        self.assertEqual(s, res)

    def test_display_2(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(9, 6)
            r1.display(9)
        self.assertEqual(
            "display() takes 1 positional argument but 2 were given", str(
                e.exception))

    def test_display_x_y(self):
        f = io.StringIO()
        r1 = Rectangle(2, 3, 2, 2)
        with contextlib.redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        res = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, res)

    def test_str(self):
        """Test for __str__ rep"""
        f = io.StringIO()
        r1 = Rectangle(4, 6, 2, 1, 12)
        with contextlib.redirect_stdout(f):
            print(r1)
        s = f.getvalue()
        res = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(s, res)

    def test_update(self):
        """Test for method update"""
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(r.update(89).id, 89)
        self.assertEqual(r.update(89, 2).width, 2)
        self.assertEqual(r.update(89, 2, 3).height, 3)
        self.assertEqual(r.update(82, 9, 3, 6).x, 6)
        self.assertEqual(r.update(2, 8, 3, 9, 5).y, 5)
        self.assertEqual(str(r.update), "[Rectangle] (2) 5/6 - 8/3")

    def test_update_string(self):
        """Test update with string argument"""
        rect = Rectangle(1, 2, 3, 4)
        with self.assertRaisesRegex(TypeError, "id must be an integer"):
            rect.update("5")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.update(4, 2, "9")

    def test_update_kwargs(self):
        """Test update method with kwargs"""
        rect = Rectangle(10, 20, 30, 40)
        rect.update(height=2)
        self.assertEqual(rect.height, 2)
        rect.update(x=2, height=4, y=6, width=8)
        self.assertEqual(rect.y, 6)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 4)

    def test_update_kwargs_strings(self):
        """Test the update method with strings args as kwargs"""
        rect = Rectangle(10, 20, 30, 40)
        with self.assertRaisesRegex(TypeError, "id must be an integer"):
            rect.update(id="2")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(height=12, x=1, width='14')

    def test_to_dictionary(self):
        """Test for the method to_dictionary"""
        rect = Rectangle(10, 20, 30, 40)
        rect_dict = rect.to_dictionary()
        rect_dict1 = {'x': 30, 'y': 40, 'id': 1, 'height': 20, 'width': 10}
        self.assertEqual(len(rect_dict), len(rect_dict1))
        self.assertEqual(type(rect_dict), dict)
        rect2 = Rectangle(12, 22)
        rect2.update(**rect_dict)
        rect_dict2 = rect2.to_dictionary()
        self.assertEqual(len(rect_dict), len(rect_dict2))
        self.assertEqual(type(rect_dict2), dict)
        self.assertFalse(rect == rect2)

    def test_to_dictionary_args(self):
        """Test with method to_dictionary with arguments"""
        mes = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 20, 30, 40)
            r.to_dictionary("3")
        self.assertEqual(mes, str(e.exception))


if __name__ == '__main__':
    unittest.main()

