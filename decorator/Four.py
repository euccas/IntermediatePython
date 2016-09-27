def four(func):
    def new_func(*args):
        return 4

    return new_func

@four
def greet(name):
    print("Hello {}".format(name))

if __name__ == "__main__":
    print(greet)
    type(greet) # <function four.<locals>.new_func at 0x1015008c8>