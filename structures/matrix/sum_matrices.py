import random


def create_matrix(rows, columns):
    matrix = []

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(random.randint(1, 10))

        matrix.append(row)
        row = []

    return matrix


rows = 5
columns = 5
matrix_a = create_matrix(rows, columns)
matrix_b = create_matrix(rows, columns)
result = create_matrix(rows, columns)

print(matrix_a)
print(matrix_b)

# Adding the matrices
for i in range(rows):
    for j in range(columns):
        result[i][j] = matrix_a[i][j] + matrix_b[i][j]

print(result)
