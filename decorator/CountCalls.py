# Python 3 approach
def count_calls(func):
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls # Must use this for decorator functions
        calls += 1
        print("called {}".format(calls))
        return func(*args, **kwargs)

    return wrapper

# Python 2 approach
def count_calls2(func):
    calls = 0

    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print("called {}".format(wrapper.calls))
        return func(*args, **kwargs)

    return wrapper

@count_calls
def add(x, y):
    return x + y

if __name__ == "__main__":
    add(1,2)
    add(2,3)
