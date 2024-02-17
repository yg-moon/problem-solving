# 출처: 이코테
from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
arr = list(map(int, input().split()))

# [left, right] 범위에 있는 데이터의 개수를 리턴
def count_in_range(arr, left, right):
    left_idx = bisect_left(arr, left)
    right_idx = bisect_right(arr, right)
    return right_idx - left_idx


# [x, x] 범위에 있는 데이터의 개수 계산
cnt = count_in_range(arr, x, x)
if cnt == 0:
    print(-1)
else:
    print(cnt)
