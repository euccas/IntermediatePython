"""
Validation Exercises

These functions return ``True`` or ``False`` depending on whether the
string passes a condition.

"""
import re


def has_vowel(string):
    """Return True iff the string contains one or more vowels."""
    return bool(re.search(r'[aeiou]', string))

def is_integer(string):
    """Return True iff the string represents a valid integer."""
    return bool(re.search(r'^-?[0-9]+$', string))

def is_fraction(string):
    """Return True iff the string represents a valid fraction."""
    return bool(re.search(r'^-?[0-9]+/0?[1-9][0-9]*$', string))
    # Other REs that work
    # r'^-?\d+/\d*[1-9]+\d*$'
    # We can also use "Look Ahead" technique to solve this, make sure the non-dominant is not 0

def is_word(string):
    """Return True iff the string represents a single word."""
    return bool(re.search(r'^[a-zA-Z-]+\'?[a-zA-Z-]*$', string))

def is_number(string):
    """Return True iff the string represents a decimal number."""
    return bool(re.search(r'^[0-9]+\.?[0-9]*$', string))

def is_hex_color(string):
    """Return True iff the string represents an RGB hex color code."""


def is_valid_date(string):
    """Return True iff the string represents a valid YYYY-MM-DD date."""


def is_ip_address(string):
    """Return True iff the string represents a valid IPv4 IP address."""


def has_word(word, sentence):
    """Return True iff sentence contains word as an individual word."""


def is_email(string):
    """Return True iff the string represents a valid email"""


def is_phone_number(string):
    """Return True iff the string represents a valid US phone number"""
