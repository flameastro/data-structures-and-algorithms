def binary_search(array, target):
    """
    O(log n) - Logarithmic

    array (in this case list) = [1, 2, 3, 4, 5]
    target = 1
    mid = 3
    ↓
    array = [1, 2]
    mid = 2
    ↓
    array = [1, 2]
    mid = 1
    return index 0
    """
    attempts = 0
    low = 0
    high = len(array)

    while low < high:
        attempts += 1

        print(array[low:high])  # Optional Line
        mid = (high + low) // 2

        if array[mid] > target:
            high = mid
        elif target > array[mid]:
            low = mid + 1
        else:
            return f"Attemps: {attempts}\nPosition: {mid}"

    else:
        return "The element is not in the array."


print(binary_search([1, 2, 3, 4, 5], 1))
