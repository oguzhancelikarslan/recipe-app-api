from app.calc import add, subtract
from django.test import TestCase


# TestCase has a bunch of helper functions that help us test our django code

class CalcTest(TestCase):
    def test_add_numbers(self):
        """ Test that two numbers are added together """
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ Test that values are subtracted and returned"""
        self.assertEqual(subtract(11, 8), 3)
