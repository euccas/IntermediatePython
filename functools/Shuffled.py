from functools import partial
import random

def shuffled(iterable):
    return sorted(iterable, key=lambda _: random.random())

# Use partial
shuffled = partial(sorted, key=lambda _: random.random())
