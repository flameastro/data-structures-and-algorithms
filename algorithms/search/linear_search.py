def linear_search(array, target):
    """
    O(n) - Linear

    array = [1, 2, 3, 4, 5]
    target = 5
    ↓
    number = 1
    1 == 5 -> False
    ↓
    number = 2
    2 == 5 -> False
    ↓
    number = 3
    3 == 5 -> False
    ↓
    number = 4
    4 == 5 -> False
    ↓
    number = 5
    5 == 5 -> True
    returns index 4
    """
    index = 0
    for number in array:
        if number == target:
            return index

        index += 1


print(linear_search([1, 2, 3, 4, 5], 5))
