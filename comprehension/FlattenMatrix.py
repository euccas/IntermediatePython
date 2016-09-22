# Flatten a Matrix
# Create a function flatten, that will take a matrix (a list of lists) and return a flattened version of the matrix.
#
# >>> matrix = [[row * 3 + incr for incr in range(1, 4)] for row in range(4)]
# >>> matrix
# [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# >>> flatten(matrix)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def flatten(matrix):
    flattened = []
    for row in matrix:
        for n in row:
            flattened.append(n)

    return flattened

def flatten2(matrix):
    # The for loop should be in the same order as you write the normal for loops
    # The order is opposite to the order when you think in English
    return [
        n
        for row in matrix
        for n in row
    ]

matrix = [[1,2,3], [4,5]]
print(flatten2(matrix))