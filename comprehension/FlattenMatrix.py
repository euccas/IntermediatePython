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