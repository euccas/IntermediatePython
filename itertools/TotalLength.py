from itertools import *

# Use chain and length

def total_length(*iterables):
    #chain(*iterables)

    #return len(list(chain.from_iterable(iterables)))

    return sum(1 for _ in chain.from_iterable(iterables)) # Not storing the list in memory, could be more efficient

if __name__ == "__main__":
    print(total_length([1,2,3], [4,5], iter([6, 7])))


