matrix = [
    [1, 2, 3, 8],
    [0, 3, 4, 5],
    [0, 0, 6, 6],
    [0, 0, 0, 10]
]
for i in range(4):
    for j in range(4):
        if i >= j:
            print(matrix[j][i])
