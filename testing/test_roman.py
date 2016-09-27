import unittest

SYMBOLS =

def roman_to_integer(numeral):
    total = []
    for symbol in numeral:
        total.append(SYMBOLS[symbol])
    return sum(total)


class RomanToIntTests(unittest.TestCase):
    def test_multiple_digits_ascending(self):
        self.verify("VIII", 8)
        self.verify("XIII", 13)
        self.verify("XXVII", 23)