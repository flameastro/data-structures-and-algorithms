import random


def create_matrix(rows, columns):
    matrix = []

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(random.randint(1, 100))

        matrix.append(row)
        row = []

    return matrix


rows = 5
columns = 5

matrix = create_matrix(rows, columns)
target = 15
position = "Not found"

for i in range(rows):
    for j in range(columns):
        if target == matrix[i][j]:
            position = i, j
            break

print(position)
