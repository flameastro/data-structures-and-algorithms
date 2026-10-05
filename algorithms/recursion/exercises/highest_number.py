# O(n)

def highest(arr):
    if len(arr) == 1:
        return arr[0]

    highest_number = highest(arr[1:])

    if arr[0] > highest_number:
        return arr[0]

    return highest_number


print(highest([1, 4, 8, 12, -8, 5, 6]))
