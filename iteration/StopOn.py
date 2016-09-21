# Stop On
# Write a generator function stop_on that accepts an iterable and a value and yields from the given iterable repeatedly until the given value is reached.

# next(iterator[, default])
# Retrieve the next item from the iterator by calling its next() method. If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.

def stop_on(numbers, value):
    for n in numbers:
        if n == value:
            break
        else:
            yield n

list(stop_on([1,2,3],3))
next(stop_on([1,2,3],3))
next(stop_on([1,2,3],3), 0)

