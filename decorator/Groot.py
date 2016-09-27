def groot(func):

    def new_func(*args):
        print("Groot")
    return new_func

@groot
def greet(name):
    print("Hello {}".format(name))

if __name__ == "__main__":
    greet("Trey")