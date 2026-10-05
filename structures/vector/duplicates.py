# O(n²)
def verify_duplicates(array):
    duplicates = []

    for x in array:
        if array.count(x) != 1 and x not in duplicates:
            duplicates.append(x)

    return duplicates


if __name__ == "__main__":
    print(verify_duplicates([1, 2, 2, 3, 4, 5, 5, 5, 4, 5, 4, 6]))  # [2, 4, 5]


# O(n²)
array = [1, 2, 2, 3, 4, 5, 5, 5, 4, 5, 4, 6]
duplicates = {x: array.count(x) for x in array if array.count(x) > 1}
print(duplicates)
