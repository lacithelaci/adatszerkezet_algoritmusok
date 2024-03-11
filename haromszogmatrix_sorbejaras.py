
matrix = [
    [1, 0, 0, 0],
    [2, 3, 0, 0],
    [4, 5, 6, 0],
    [7, 8, 9, 10]
]

for i in range(4):
    for j in range(4):
        if i >= j:
            print(matrix[i][j])

