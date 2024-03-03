def search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            return m
    return -1
