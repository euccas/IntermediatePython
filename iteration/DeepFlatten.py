def deep_flatten(iterable):
    flattened = []

    for n in iterable:
        try:
            flattened += deep_flatten(n) # += is same as extend()
        except TypeError:
            flattened.append(n)

    return flattened

def deep_flatten2(iterable):

    for n in iterable:
        try:
            yield from deep_flatten2(n)
            #for x in deep_flatten2(n):
            #    yield x

        except TypeError:
            yield n

print(list(deep_flatten([0, [1, [2, 3]], [4]])))
print(list(deep_flatten2([0, [1, [2, 3]], [4]])))