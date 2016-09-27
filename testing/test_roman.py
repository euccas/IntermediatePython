import unittest
from roman import roman_to_int

class RomanToIntTests(unittest.TestCase):

    def verify(self, numeral, integer):
        self.assertEqual(roman_to_int(numeral), integer)

    def test_invalid_characters(self):
        self.assertRaises(ValueError, roman_to_int, "E")
        # with self.assertRaises(ValueError):
        #    roman_to_int("E")

    def test_multiple_digits_ascending(self):
        self.verify("VIII", 8)
        self.verify("XIII", 13)
        self.verify("XXVII", 23)