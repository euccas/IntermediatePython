"""
Search Exercises

These functions return a list of strings matching a condition.

"""
import re


with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()


def get_4_letter_words(string):
    """Return all four letter words found in the given string."""


def get_email(string):
    """Search the string for a valid email and return it; else return None."""


def get_extension(filename):
    """Return the file extension for a full file path."""
    return re.search(r'^(.*\.)+(.*)$', filename).group(2)

def hexadecimal(dictionary=dictionary):
    """Return a list of all words consisting solely of the letters A to F."""
    return re.findall(r'\b[abcdef]+\b', dictionary, re.IGNORECASE)


def tetravocalic(dictionary=dictionary):
    """Return a list of all words that have four consecutive vowels."""


def hexaconsonantal(dictionary=dictionary):
    """Return a list of all words with six consecutive consonants."""


def possible_words(partial_word, dictionary=dictionary):
    """
    Return possible word matches from a partial word.

    Underscores in partial words represent missing letters.  Examples:
        C_T (cat, cot, cut)
        _X_ (axe)
    """


def five_repeats(letter, dictionary=dictionary):
    """Return all words with at least five occurrences of the given letter."""


def abbreviate(phrase):
    """Return an acronym for the given phrase."""


def palindrome5(dictionary=dictionary):
    """Return a list of all five letter palindromes."""


def double_double(dictionary=dictionary):
    """
    Return words with a double repeated letter with one letter between.

    Example double double words:
    - freebee
    - assessed
    - voodoo
    """


def repeaters(dictionary=dictionary):
    """
    Return words that consist of the same letters repeated two times.

    Example double double words:
    - tutu
    - cancan
    - murmur
    """
