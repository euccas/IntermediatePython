import math

numbers = range(101)

cube_of_squares = []
for n in numbers:
    if math.sqrt(n).is_integer():
        cube_of_squares.append(n**3)

print(cube_of_squares)

# List comprehension
cube_of_squares_2 = [
    n ** 3
    for n in numbers
    if math.sqrt(n).is_integer()
]

print(cube_of_squares_2)

def is_perfect_square(n):
    return math.sqrt(n).is_integer()

cube_of_squares_3 = [
    n ** 3
    for n in numbers
    if is_perfect_square(n)
]

print(cube_of_squares_3)