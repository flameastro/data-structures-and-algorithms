# O(n)

def search(arr, value, index = 0):
    if not arr:
        return "Value not in the list"

    if arr[0] == value:
        return index

    return search(arr[1:], value, index + 1)


print(search([1, 2, 3], 2))  # 1
print(search([1, 2, 3], 5))  # Value not in the list
