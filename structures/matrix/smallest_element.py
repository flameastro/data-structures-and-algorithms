def create_matrix(rows, columns):
    matrix = []

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(None)

        matrix.append(row)
        row = []

    return matrix


rows = 4
columns = 3
matrix = create_matrix(rows, columns)

for i in range(rows):
    for j in range(columns):
        value = int(input(f"{i, j}: "))
        matrix[i][j] = value


# Smallest
smallest = matrix[0][0]
smallest_position = [0, 0]

for i in range(rows):
    for j in range(columns):
        if smallest > matrix[i][j]:
            smallest = matrix[i][j]
            smallest_position = [i, j]

print(smallest, smallest_position)
