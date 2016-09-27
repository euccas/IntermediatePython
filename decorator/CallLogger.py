def call_logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        value = func(*args, **kwargs)
        print("Function returned")
        return value
    return wrapper

def greet(name):
    print("Hello {}".format(name))

if __name__ == "__main__":
    greet = call_logger(greet)
    @call_logger
    def greet(name):
        print("Hello {}".format(name))

