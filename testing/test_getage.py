import unittest
from unittest.mock import patch
import datetime
from testing.birthday_utils import *

class GetAgeTests(unittest.TestCase):

    """Tests for get_age function."""

    def test_born_yesterday(self):
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        self.assertEqual(get_age(birthdate=yesterday), 0)

    def test_ten_years_old(self):
        today = datetime.date.today()
        ten_years_ago = today.replace(year=today.year - 10)
        self.assertEqual(get_age(birthdate=ten_years_ago), 10)

    def test_ten_years_old_tomorrow(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        ten_years_ago_tomorrow = tomorrow.replace(year=tomorrow.year - 10)
        self.assertEqual(get_age(birthdate=ten_years_ago_tomorrow), 9)

    def test_born_on_leap_day(self):
        with patch('testing.birthday_utils.get_today') as get_today:
            get_today.return_value = datetime.date(2010, 2, 28)
            birthdate = datetime.date(2000, 2, 29)
            self.assertEqual(get_age(birthdate=birthdate), 9)

if __name__ == "__main__":
    unittest.main()