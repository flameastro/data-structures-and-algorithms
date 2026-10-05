def bubble_sort(array):
    """
    O(n²) - Quadratic

    [5, 1, 2, 7, 3]
    Starting from first position (element 5)
    ↓
    5 > 1
    5 and 1 swaps they position
    ↓
    [1, 5, 2, 7, 3]
    ↓
    5 > 2
    5 and 2 swaps they position
    ↓
    [1, 2, 5, 7, 3]
    ↓
    5 < 7
    5 and 7 stays on his position
    ↓
    7 > 3
    7 and 3 swaps they position
    ↓
    [1, 2, 5, 3, 7]
    Repeats again, starting from position 2 (element 2)
    ↓
    [1, 2, 5, 3, 7]
    5 > 3 
    5 and 3 swaps they position
    ↓
    [1, 2, 3, 5, 7]
    5 < 7
    They stay on they position
    Repeats again, starting from position 3 (element 3)
    3 < 5
    They stay
    5 < 7
    They stay
    Repeats again, starting from position 4 (element 5)
    5 < 7
    They stay

    End, returning the new array with the correct positions
    """
    for x in range(len(array)):
        for item in range(len(array) - 1):
            if array[item] > array[item + 1]:
                aux = array[item]
                array[item] = array[item + 1]
                array[item + 1] = aux

    return array


print(bubble_sort([3, 2, 1]))
