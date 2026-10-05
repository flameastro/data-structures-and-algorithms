# First soluction: Create a new array and put all elements there if the element its not x
#  O(n)

def solution1(array, x):
    new_array = []

    for i in range(len(array)):
        if array[i] != x:
            new_array.append(array[i])

    return new_array


print(solution1([1, 2, 3, 4, 5], 3))


# ! Second solution: Iterate through the array and search for x. If it is found, perform another iteration to swap the elements. As a result, the desired element will be moved to the last position. After the for j loop finishes, we remove the last element from the array, resulting in all the other elements remaining in their original order, with x removed.

# It uses O(n) × 2, so the overall time complexity is O(n).

def solution2(array, x):
    found = False

    for i in range(len(array)):
        if array[i] == x:
            for j in range(len(array[i+1:])):
                troca = array[i]
                array[i] = array[i+1]
                array[i+1] = troca
                i += 1
                found = True

            break

    if found:
        array = array[:-1]

    return array


print(solution2([1, 2, 3, 4, 5], 3))
