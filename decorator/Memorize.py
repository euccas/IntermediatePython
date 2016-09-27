from functools import wraps

def memorize(func):
    cache = {}
    @wraps(func)
    def new_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    new_func.cache = cache
    return new_func

