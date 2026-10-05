# O(n)

def count_occurrences(arr, n):
    if not arr:
        return 0

    if arr[0] == n:
        return 1 + count_occurrences(arr[1:], n)
    else:
        return count_occurrences(arr[1:], n)


print(count_occurrences([1, 2, 2, 3, 2], 2))  # 3
