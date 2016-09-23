# Random Number
# Make an inexhaustable iterator object RandomNumberGenerator that always provides 4 as the next number.
#
# Example:
#
# >>> number_generator = RandomNumberGenerator()
# >>> next(number_generator)
# 4
# >>> next(number_generator)
# 4
# >>> next(number_generator)
# 4
# >>> iter(number_generator) is number_generator
# True
#
# This is just a duck typing class. Fulfilling Iterator protocol.

class RandomNumberGenerator:

    def __iter__(self):
        return self

    def __next__(self):
        return 4

