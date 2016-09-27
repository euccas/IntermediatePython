from contextlib import contextmanager

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

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args, **kwargs):
        import pdb; pdb.set_trace()
        self.close()
