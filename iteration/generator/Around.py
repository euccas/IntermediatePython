# Around
# Write a generator function around that accepts an iterable and yields a tuple containing the previous item, the current item, and the next item. The previous item should start at None and the next item should be None for the last item in the iterable.
#
# Example:
#
# >>> list(around([1, 2, 3, 4]))
# [(None, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, None)]
# >>> list(around([]))
# []
# >>> list(around("hey"))
# [(None, 'h', 'e'), ('h', 'e', 'y'), ('e', 'y', None)]

# Solution around only works on sequences
def around(iterable):
    for i in range(len(iterable)):
        try:
            if i == 0:
                yield((None, iterable[i], iterable[i+1]))
            else:
                yield((iterable[i-1], iterable[i], iterable[i+1]))
        except IndexError:
             if i == 0:
                yield((None, iterable[i], None))
             else:
                yield((iterable[i-1], iterable[i], None))

# This is the ideal solution
def around2(elements):
    previous, current = None, None
    for next_item in elements:
        if current:
            yield previous, current, next_item
        previous, current = current, next_item
    if current:
        yield previous, current, None

print(list(around([1,2,3,4])))
print(list(around([])))
print(list(around("hey")))