def binary_search(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            return m

    return -1


sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(sorted_arr, 7))

"""
- 목표: 타겟의 인덱스
- 주의: 정렬된 배열에만 사용 가능!
"""
