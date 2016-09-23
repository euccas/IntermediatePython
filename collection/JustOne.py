class JustOne:

    def __contains__(self, value):
    # optional
        if value == 1:
            return True
        return False
        # return (value == 1)

    def __len__(self):
        return 1

    #def __iter__(self):
    #    return iter([1])

    def __iter__(self):
       yield 1

    def __next__(self):
    # optional
        return 1

    def __getitem__(self, i):
        return 1

    def __bool__(self):
    # optional
        return True