class suppress:
    def __init__(self, exception_type):
        self.exception_type = exception_type

    def __enter__(self):
        pass

    def __exit__(self, exception_type, exception, traceback):
        print(exception_type, )
        if issubclass(exception_type, self.exception_type):
            return True

if __name__ == "__main__":
    int(None)


