from collections import UserList

class CyclicList:
    def __getitem__(self, key):
        return self.data[key % len(self.data)]

