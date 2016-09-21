# Easy Dict
#
# Make an EasyDict class that can be used with both attribute and item syntax.
#
# Example:
#
# >>> a = EasyDict()
# >>> a['shoe'] = "blue"
# >>> a.shoe
# "blue"
# >>> a['shoe']
# "blue"
# >>> a.car = "green"
# >>> a['car']
# "green"
# >>> a.red
# "AttributeError: 'EasyDict' object has no attribute 'red'"
#
# Hint:
# The __dict__ attribute is a dictionary which stores all attributes in a class.
#
# >>> class A:
# ...     pass
# ...
# >>> a = A()
# >>> a.__dict__
# {}
# >>> a.hello = "there"
# >>> a.__dict__
# {'hello': 'there'}
#
# Use the __getitem__ and __setitem__ methods

class EasyDict:
    def __init__(self):
        pass

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)