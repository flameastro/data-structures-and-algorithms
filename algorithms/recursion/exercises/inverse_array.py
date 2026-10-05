# O(n)

def inverse(arr):
    if not arr:
        return arr

    return inverse(arr[1:]) + [arr[0]]


print(inverse([1, 2, 3, 4]))  # [4, 3, 2, 1]
