#!/usr/bin/python3
"""
Unittest Base.
Test cases for Base class.
Test cases are done based on the no of tasks
(i.e 'test_1' is for test of task 1)
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for the Base class."""

    def setUp(self):
        self._Base__nb_objects = 0

    def test_1(self):
        """create new instances: check for id."""

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
        b6 = Base(0)
        self.assertEqual(b6.id, 0)
        b7 = Base(-9)
        self.assertEqual(b7.id, -9)

    def test_1_1(self):
        """Test for type and instance"""

        b8 = Base()
        self.assertTrue(isinstance(b8, Base))


if __name__ == '__main__':
    unittest.main()
