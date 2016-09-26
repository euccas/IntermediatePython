# Unique
# Create a generator function that takes an iterable and yields the iterable elements in order, skipping duplicate values.
#
# Example:
#
# >>> list(unique([6, 7, 0, 9, 0, 1, 2, 7, 7, 9]))
# [6, 7, 0, 9, 1, 2]
# >>> list(unique([]))
# []
# >>> ''.join(unique("hello there"))
# 'helo tr'

# This unique function removes any item if it has duplications
def unique(iterable):
    record = dict()
    for i in iterable:
        if not i in record:
            record[i] = 1
        else:
            record[i] += 1

    for x in record:
        if record[x] == 1:
            yield x

print(list(unique([6, 7, 0, 9, 0, 1, 7])))
print(list(unique([])))
print(''.join(unique("hello there")))

# This unique2 function keeps only one item if it has duplications
def unique2(iterable):
    record = []
    for i in iterable:
        if not i in record:
            record.append(i)
            yield i

print(list(unique2([6, 7, 0, 9, 0, 1, 7])))
print(list(unique2([])))
print(''.join(unique2("hello there")))


