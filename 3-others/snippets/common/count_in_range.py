from bisect import bisect_left, bisect_right


def count_in_range(arr, l, r):
    return bisect_right(arr, r) - bisect_left(arr, l)


sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(count_in_range(sorted_arr, 3, 8))

"""
- 목표: 값이 [left, right] 범위에 있는 데이터의 개수
- 주의: 정렬된 배열에만 사용 가능
"""
