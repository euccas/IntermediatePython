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

# def pairwise(iterable):
#     while True:
#         i = iter(iterable)
#         try:
#             curr = next(i)
#             cnext = next(i)
#             yield(curr, cnext)
#         except StopIteration:
#             yield(curr, None)

def pairwise(iterable):
    for i in range(len(iterable)):
        try:
            yield(iterable[i], iterable[i+1])
        except IndexError:
            yield(iterable[i], None)

print(list(pairwise([1,2,3])))
print(list(pairwise("hey")))
print(list(pairwise([])))
