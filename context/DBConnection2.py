from contextlib import contextmanager

## When using contextmanager, the class does not need have __exit__ and __enter__ methods.

@contextmanager
def nothing():
    print("entering block")
    try:
        yield
    finally:
        print("exiting block")

@contextmanager
def open_db(name):
    db = DBConnection(name)
    try:
        db.open()
        yield db
    finally:
        db.close()

class DBConnection:
    def __init__(self, name):
        self.name = name

    def open(self):
        print("Connecting to database {}".format(self.name))

    def close(self):
        print("Disconnecting from database {}".format(self.name))

if __name__ == "__main__":
    with open_db("Trey") as db:
        print(db.name)
