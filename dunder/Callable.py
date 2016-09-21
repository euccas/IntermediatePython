# Is Callable
#
# Implement a function, accept any object
#
# Example:
# >>> is_callable(sorted)
# True
# >>> is_callable(str)
# True
# >>> is_callable(4)
# False

def is_callable(obj):

    try:
        obj.__call__
        # hasattr(str, '__call__')
        # getattr(str, '__call__')
    except AttributeError:
        return False
    else:
        return True

