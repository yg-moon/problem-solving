from bisect import bisect_left, bisect_right


# 목표: [left, right] 범위에 있는 데이터의 개수
# 주의: 정렬된 배열에만 사용
def cnt_in_range(arr, l, r):
    return bisect_right(arr, r) - bisect_left(arr, l)


# Test
sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(cnt_in_range(sorted_arr, 3, 8))
