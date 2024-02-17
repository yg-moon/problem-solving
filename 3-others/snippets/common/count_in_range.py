from bisect import bisect_left, bisect_right


# [left, right] 범위에 있는 데이터의 개수를 리턴
def count_in_range(arr, left, right):
    left_idx = bisect_left(arr, left)
    right_idx = bisect_right(arr, right)
    return right_idx - left_idx
