# Hypotenuse
## Make a function that returns the hypotenuse of a right triangle given the other two sides

def get_hypotenuse(a, b):
    c2 = a ** 2 + b ** 2
    c = "{:.1f}".format(c2 ** 0.5) # Hint: to get the square root of a number, raise it to the power of 0.5
    # same as
    # '%.2f' % (c2 ** 0.5)
    return c

print(get_hypotenuse(3,4))
print(get_hypotenuse(5,12))

