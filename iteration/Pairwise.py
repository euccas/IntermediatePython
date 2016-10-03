# Pairwise
# Write a generator function pairwise that accepts an iterable and yields a tuple containing each item and the item following it. The last item should treat the item after it as None.
#
# Example:
#
# >>> list(pairwise([1, 2, 3]))
# [(1, 2), (2, 3), (3, None)]
# >>> list(pairwise([]))
# []
# >>> list(pairwise("hey"))
# [('h', 'e'), ('e', 'y'), ('y', None)]

# def pairwise(iterable):
#     for i in iterable:
#         try:
#             i_next = next(iter(i))
#         except StopIteration:
#             i_next = None
#         yield(i, i_next)

def pairwise(iterable):
    i = iter(iterable)
    stop = False
    while not stop:
        curr = next(i)
        try:
            cnext = next(i)
        except StopIteration:
            cnext = None
            stop = True
        yield(curr, cnext)

# def pairwise(iterable):
#     for i in range(len(iterable)):
#         try:
#             yield(iterable[i], iterable[i+1])
#         except IndexError:
#             yield(iterable[i], None)

print(list(pairwise([1,2,3])))
print(list(pairwise("hey")))
print(list(pairwise([])))

def pairwise2(elements):
    previous, current = None, None
    for current in elements:
        if previous:
            yield previous, current
        previous = current
    if current:
        yield current, None

# Another solution which only works on sequences
def pairwise3(elements):
    for i, item in enumerate(elements):
        if i < len(elements) - 1:
            next_item = elements[i+1]
        else:
            next_item = None
        yield item, next_item