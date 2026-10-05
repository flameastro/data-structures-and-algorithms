# O(n)

def arr_sum(arr):
    if not arr:
        return 0

    return arr[0] + arr_sum(arr[1:])


print(arr_sum([1, 2, 3, 4, 5])) # 15
