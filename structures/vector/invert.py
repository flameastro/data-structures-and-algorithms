# O(n)
def invert(array):
    for i in range(1, (len(array) // 2) + 1):
        aux = array[i - 1]
        array[i - 1] = array[-i]
        array[-i] = aux

    return array


if __name__ == "__main__":
    print(invert([1, 2, 3]))
    print(invert([1, 2, 3, 4]))
    print(invert([5, 4, 1, 2, 4, 3, 6, 5, 1, 2, 3, 8, 7, 3, 2, 1]))
