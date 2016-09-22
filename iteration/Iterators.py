def first(iterable):
    i = iter(iterable)
    return next(i)

def first2(iterable, default=None):
    return next(iter(iterable), default)

def is_iterator(item):
    i = iter(item)
    if i is item:  # should check identify, so do not use == here
        return True
    return False
