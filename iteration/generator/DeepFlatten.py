# Deep Flatten
# Write a function that “flattens” nested iterables. In other words the function should accept an iterable of iterables and yield non-iterable items in order.
#
# Example:
#
# >>> list(flatten([0, [1, [2, 3]], [4]]))
# [0, 1, 2, 3, 4]
# >>> list(flatten([[()]]))
# []

def deep_flatten(iterable):
    flattened = []

    for n in iterable:
        if isinstance(n, (str, bytes)):
            flattened.append(n)
        else:
            try:
                # += is same as extend()
                flattened += deep_flatten(n)
            except TypeError:
                flattened.append(n)

    return flattened

def deep_flatten2(iterable):

    for n in iterable:
        if isinstance(n, (str, bytes)):
            yield n
        else:
            try:
                yield from deep_flatten2(n)
                #for x in deep_flatten2(n):
                #    yield x

            except TypeError:
                yield n

print(list(deep_flatten([0, [1, [2, 3]], [4]])))
print(list(deep_flatten(["hello", [1,2], 3, 4])))

#print(list(deep_flatten2([0, [1, [2, 3]], [4]])))
#print(list(deep_flatten2(["hello", [1,2], 3, 4])))

## Reference Solutions
## Notes: try except should be around the loop

def flatten(iterable):
    try:
        for item in iterable:
            yield from flatten(item)
    except TypeError:
        yield iterable

def flatten2(iterable):
    try:
        for item in iterable:
            if isinstance(item, (str, bytes)):
                yield item
            else:
                yield from flatten2(item)
    except TypeError:
        yield iterable

