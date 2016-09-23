def is_perfect_cube(n):
    return round(n ** (1/3)) ** 3 == n

def FindCube(numbers):
    return [
        n
        for n in numbers
        if is_perfect_cube(n)
    ]

def FindCube2(numbers):
    for n in numbers:
        if is_perfect_cube(n):
            return n

numbers = range(100000000, )
print(FindCube2(numbers))