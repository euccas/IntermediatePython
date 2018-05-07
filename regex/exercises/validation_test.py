"""Tests for validation exercises"""
import unittest


from validation import (has_vowel, is_integer, is_fraction, is_word, is_number,
                        is_hex_color, is_valid_date, is_ip_address, has_word,
                        is_email, is_phone_number)


class HasVowelTests(unittest.TestCase):

    def test_rhythm(self):
        self.assertFalse(has_vowel("rhythm"))

    def test_exit(self):
        self.assertTrue(has_vowel("exit"))

    def test_no(self):
        self.assertTrue(has_vowel("no"))

    def test_yes(self):
        self.assertTrue(has_vowel("yes"))

    def test_fly(self):
        self.assertFalse(has_vowel("fly"))

    def test_symbols(self):
        self.assertFalse(has_vowel("%^&"))

    def test_empty(self):
        self.assertFalse(has_vowel(""))


class IsIntegerTests(unittest.TestCase):

    def test_single_digit(self):
        self.assertTrue(is_integer("5"))

    def test_leading_letter(self):
        self.assertFalse(is_integer("a5"))

    def test_trailing_letter(self):
        self.assertFalse(is_integer("5a"))

    def test_5000(self):
        self.assertTrue(is_integer("5000"))

    def test_leading_minus(self):
        self.assertTrue(is_integer("-999"))

    def test_leading_plus(self):
        self.assertFalse(is_integer("+999"))

    def test_leading_zero(self):
        self.assertTrue(is_integer("00"))

    def test_zero_decimal(self):
        self.assertFalse(is_integer("0.0"))

    def test_only_minus(self):
        self.assertFalse(is_integer("-"))

    def test_leading_space(self):
        self.assertFalse(is_integer(" 5"))

    def test_empty(self):
        self.assertFalse(is_integer(""))


class IsFractionTests(unittest.TestCase):

    def test_5000(self):
        self.assertFalse(is_fraction("5000"))

    def test_leading_minus(self):
        self.assertTrue(is_fraction("-999/1"))

    def test_leading_plus(self):
        self.assertFalse(is_fraction("+999/1"))

    def test_leading_zero_in_numerator(self):
        self.assertTrue(is_fraction("00/1"))

    def test_no_numerator(self):
        self.assertFalse(is_fraction("/5"))

    def test_no_denominator(self):
        self.assertFalse(is_fraction("5/"))

    def test_divide_by_zero(self):
        self.assertFalse(is_fraction("5/0"))

    def test_leading_zero_in_denominator(self):
        self.assertTrue(is_fraction("5/010"))

    def test_simple_fraction(self):
        self.assertTrue(is_fraction("5/105"))

    def test_with_spaces(self):
        self.assertFalse(is_fraction("5 / 1"))

    def test_empty(self):
        self.assertFalse(is_fraction(""))

    def test_leading_letter(self):
        self.assertFalse(is_fraction("a5"))

    def test_trailing_letter(self):
        self.assertFalse(is_fraction("5a"))


class IsWordTests(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(is_word(""))

    def test_capitalized(self):
        self.assertTrue(is_word("Trey"))

    def test_with_space(self):
        self.assertFalse(is_word("ice cream"))

    def test_one_word(self):
        self.assertTrue(is_word("ice"))
        self.assertTrue(is_word("cream"))

    def test_apostrophe(self):
        self.assertTrue(is_word("don't"))

    def test_hyphen(self):
        self.assertTrue(is_word("self-report"))

    def test_period(self):
        self.assertFalse(is_word("No."))

    def test_comma(self):
        self.assertFalse(is_word("yes,"))

    def test_question_mark(self):
        self.assertFalse(is_word("what?"))

    def test_exclamation_mark(self):
        self.assertFalse(is_word("what!"))

    def test_digits(self):
        self.assertFalse(is_word("hell0"))

    def test_underscore(self):
        self.assertFalse(is_word("not_a_word"))


class IsNumberTests(unittest.TestCase):

    def test_5(self):
        self.assertTrue(is_number("5"))

    def test_5_point(self):
        self.assertTrue(is_number("5."))

    def test_point_5_point(self):
        self.assertFalse(is_number(".5."))

    def test_point_5(self):
        self.assertTrue(is_number(".5"))

    def test_leading_zero(self):
        self.assertTrue(is_number("01.5"))

    def test_negative(self):
        self.assertTrue(is_number("-123.859"))

    def test_two_decimals(self):
        self.assertFalse(is_number("-123.859."))

    def test_just_a_decimal(self):
        self.assertFalse(is_number("."))

    def test_leading_garbage(self):
        self.assertFalse(is_number("a5"))

    def test_trailing_garbage(self):
        self.assertFalse(is_number("5a"))


class IsHexColorTests(unittest.TestCase):

    def test_purple_short(self):
        self.assertTrue(is_hex_color("#639"))

    def test_four_digits(self):
        self.assertFalse(is_hex_color("#6349"))

    def test_five_digits(self):
        self.assertFalse(is_hex_color("#63459"))

    def test_dark_purple(self):
        self.assertTrue(is_hex_color("#634569"))

    def test_purple_long(self):
        self.assertTrue(is_hex_color("#663399"))

    def test_black(self):
        self.assertTrue(is_hex_color("#000000"))

    def test_two_digits(self):
        self.assertFalse(is_hex_color("#00"))

    def test_mixed_case(self):
        self.assertTrue(is_hex_color("#FFffFF"))

    def test_hex(self):
        self.assertTrue(is_hex_color("#decaff"))

    def test_invalid_character(self):
        self.assertFalse(is_hex_color("#decafz"))

    def test_no_octothorpe(self):
        self.assertFalse(is_hex_color("639"))

    def test_misplaced_octothorpe(self):
        self.assertFalse(is_hex_color("639#"))

    def test_leading_garbage(self):
        self.assertFalse(is_hex_color("a#639"))


class IsValidDateTests(unittest.TestCase):

    def test_this_year(self):
        self.assertTrue(is_valid_date("2016-01-02"))

    def test_1990(self):
        self.assertTrue(is_valid_date("1900-01-01"))

    def test_invalid_day(self):
        self.assertFalse(is_valid_date("2016-02-99"))

    def test_invalid_year(self):
        self.assertFalse(is_valid_date("20-02-20"))

    def test_invalid_month(self):
        self.assertFalse(is_valid_date("1980-30-05"))

    def test_leading_garbage(self):
        self.assertFalse(is_valid_date("12016-01-02"))

    def test_trailing_garbage(self):
        self.assertFalse(is_valid_date("2016-01-020"))


class IsIPAddressTests(unittest.TestCase):

    def test_local_ip(self):
        self.assertTrue(is_ip_address("192.168.1.1"))

    def test_spaces(self):
        self.assertFalse(is_ip_address("192.168.1.1 "))
        self.assertFalse(is_ip_address(" 192.168.1.1"))

    def test_google_dns(self):
        self.assertTrue(is_ip_address("8.8.8.8"))

    def test_localhost(self):
        self.assertTrue(is_ip_address("127.0.0.1"))

    def test_mixed_length_ip(self):
        self.assertTrue(is_ip_address("74.118.212.1"))

    def test_too_large_numbers(self):
        self.assertFalse(is_ip_address("999.999.999.999"))
        self.assertFalse(is_ip_address("256.1.1.1"))
        self.assertFalse(is_ip_address("1.355.1.1"))
        self.assertFalse(is_ip_address("1.1.260.1"))

    def test_edge_cases(self):
        self.assertTrue(is_ip_address("255.255.255.255"))
        self.assertTrue(is_ip_address("0.0.0.0"))

    def test_too_few_numbers(self):
        self.assertFalse(is_ip_address("8.8.8"))
        self.assertFalse(is_ip_address("8.8"))

    def test_too_many_numbers(self):
        self.assertFalse(is_ip_address("8.8.8.8.8"))


class HasWordTests(unittest.TestCase):

    def test_just_the_word(self):
        sentence = "help"
        self.assertTrue(has_word("help", sentence))

    def test_different_capitalization(self):
        sentence = "Help"
        self.assertTrue(has_word("help", sentence))

    def test_whole_word_mid_sentence(self):
        sentence = "She was a big help when I learned French"
        self.assertTrue(has_word("help", sentence))

    def test_punctuation(self):
        sentence = "Help! I need somebody."
        self.assertTrue(has_word("help", sentence))

    def test_word_prefix(self):
        sentence = "She helped me learn French"
        self.assertFalse(has_word("help", sentence))

    def test_word_suffix(self):
        sentence = "feel"
        self.assertFalse(has_word("eel", sentence))


class IsEmailTests(unittest.TestCase):

    def test_digits(self):
        self.assertTrue(is_email("123@example.com"))

    def test_plus(self):
        self.assertTrue(is_email("myname+spam@gmail.com"))

    def test_subdomain(self):
        self.assertTrue(is_email("info@help.example.com"))

    def test_subdomain(self):
        self.assertTrue(is_email("info@help.example.com"))

    def test_long_tld(self):
        self.assertTrue(is_email("me@something.technology"))

    def test_short_email(self):
        self.assertTrue(is_email("a@b.co"))

    def test_symbols(self):
        self.assertTrue(is_email("my_name+with%symbols@b.com"))

    def test_capitals(self):
        self.assertTrue(is_email("A@BCD.COM"))

    def test_single_letter_tld(self):
        self.assertFalse(is_email("123@example.c"))

    def test_no_name(self):
        self.assertFalse(is_email("@b.co"))

    def test_no_domain(self):
        self.assertFalse(is_email("a@.co"))

    def test_no_period(self):
        self.assertFalse(is_email("a@abcd"))


class IsPhoneNumberTests(unittest.TestCase):

    def test_no_punctuation(self):
        self.assertTrue(is_phone_number("8885557777"))

    def test_dashes(self):
        self.assertTrue(is_phone_number('202-762-1401'))

    def test_parenthesis_without_space(self):
        self.assertTrue(is_phone_number('(202)762-1401'))

    def test_parenthesis_with_space(self):
        self.assertTrue(is_phone_number('(202) 762-1401'))

    def test_periods(self):
        self.assertTrue(is_phone_number('202 . 762 . 1401'))

    def test_incorrect_dash_placement(self):
        self.assertFalse(is_phone_number('20-2762-1401'))

    def test_letters(self):
        self.assertFalse(is_phone_number('123-456-78A9'))

    def test_too_short(self):
        self.assertFalse(is_phone_number('123456789'))

    def test_too_long(self):
        self.assertFalse(is_phone_number('12345678901'))

    def test_incorrect_period_placement(self):
        self.assertFalse(is_phone_number('123 . 4567 . 890'))


if __name__ == "__main__":
    raise SystemExit("No CLI for this file.  Run test.py instead.")
