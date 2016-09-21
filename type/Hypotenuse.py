def get_hypotenuse(a, b):
    c2 = a ** 2 + b ** 2
    c = c2 ** 0.5 # Hint: to get the square root of a number, raise it to the power of 0.5
    return c

print(get_hypotenuse(3,4))