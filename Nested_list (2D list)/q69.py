"""
Q69. Given a 3x3 matrix as input, print its lower triangle.
Replace all elements in the upper triangle (above the main diagonal) with an asterisk (*).

1  2  3
4  5  6
7  8  9

1  *  *
4  5  *
7  8  9
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

rows = len(matrix)
col = len(matrix[0])
for i in range(0, rows):
    for j in range(0, col):
        if j >= i + 1:
            print("*", end=" ")
        else:
            print(matrix[i][j], end=" ")
    print()
