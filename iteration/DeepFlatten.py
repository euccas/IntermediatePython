def deep_flatten(iterable):
    flattened = []

    for n in iterable:
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
print(list(deep_flatten2([0, [1, [2, 3]], [4]])))
print(list(deep_flatten(["hello", [1,2], 3, 4])))
print(list(deep_flatten2(["hello", [1,2], 3, 4])))