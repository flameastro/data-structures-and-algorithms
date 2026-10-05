def selection_sort(arr):
    """
    O(n²) - Quadratic

    [5, 1, 2, 7, 3]

    Starting from first position (element 5)
    ↓
    We look for the smallest element in the rest of the array
    ↓
    1 is the smallest
    ↓
    5 and 1 swap their positions
    ↓
    [1, 5, 2, 7, 3]

    Starting from position 2 (element 5)
    ↓
    We look for the smallest element in the rest of the array
    ↓
    2 is the smallest
    ↓
    5 and 2 swap their positions
    ↓
    [1, 2, 5, 7, 3]

    Starting from position 3 (element 5)
    ↓
    We look for the smallest element in the rest of the array
    ↓
    3 is the smallest
    ↓
    5 and 3 swap their positions
    ↓
    [1, 2, 3, 7, 5]

    Starting from position 4 (element 7)
    ↓
    5 is the smallest
    ↓
    7 and 5 swap their positions
    ↓
    [1, 2, 3, 5, 7]

    End, returning the new array with the correct positions
    """

    pos = 0

    for _ in range(len(arr)):
        smallest = arr[pos]
        pos_smallest = pos

        for i in range(pos, len(arr)):
            if smallest > arr[i]:
                smallest = arr[i]
                pos_smallest = i

        aux = arr[pos]
        arr[pos] = smallest
        arr[pos_smallest] = aux

        pos += 1

    return arr


print(selection_sort([15, 12, 27, 23, 7, 2, 0, 18, 19, 21]))
