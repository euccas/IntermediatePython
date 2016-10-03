# This program prints dots representing fibonacci numbers until the width of the terminal is reached.
#
# Refactor this program to use a for loop and a generator function:
#
# import os
#
# if __name__ == "__main__":
#     text_width = 5
#     limit = os.get_terminal_size().columns - text_width
#     a, b = 0, 1
#     while a <= limit:
#         print("{} ".format(a).rjust(text_width), end="")
#         print("." * a)
#         a, b = b, a+b

import os

def get_fibonacci_until(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    text_width = 5
    limit = os.get_terminal_size().columns - text_width
    for n in get_fibonacci_until(limit):
        print("{} ".format(n).rjust(text_width), end="")
        print("." * n)
