def create_matrix(rows, columns):
    matrix = []

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(None)

        matrix.append(row)
        row = []

    return matrix


rows = 3
columns = 2
matrix = create_matrix(rows, columns)


for i in range(rows):
    for j in range(columns):
        value = int(input())
        matrix[i][j] = value

print(matrix)
