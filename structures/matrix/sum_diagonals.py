def fill_matrix(rows, columns):
    matrix = []

    for _ in range(rows):
        temp = []
        for _ in range(columns):
            value = int(input())
            temp.append(value)

        matrix.append(temp)
        temp = []

    return matrix


def sum_main_diagonal(columns, matrix):
    total = 0
    row = 0
    column = 0

    for i in range(columns):
        total += matrix[row][column]
        row += 1
        column += 1

    return total


def sum_secondary_diagonal(rows, columns, matrix):
    total = 0
    row = 0
    column = columns - 1

    for i in range(rows):
        total += matrix[row][column]
        row += 1
        column -= 1

    return total


def print_matrix(rows, columns, matrix):
    for i in range(rows):
        for j in range(columns):
            print(f"{matrix[i][j]}", end=" ")

        print("\n")


rows = 4
columns = 4
matrix = fill_matrix(rows, columns)

print_matrix(rows, columns, matrix)
print(sum_main_diagonal(columns, matrix))
print(sum_secondary_diagonal(rows, columns, matrix))
