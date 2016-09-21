def first(iterable):
    i = iter(iterable)
    return next(i)

def is_iterator(item):
    i = iter(item)
    if i is item:
        return True
    return False
