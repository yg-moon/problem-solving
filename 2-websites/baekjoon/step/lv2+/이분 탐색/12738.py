# 가장 긴 증가하는 부분 수열3
# 출처: https://bio-info.tistory.com/116
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

lis = []

for num in arr:
    idx = bisect_left(lis, num)
    if len(lis) == idx:
        lis.append(num)
    else:
        lis[idx] = num

print(len(lis))

"""
- 난이도: 골드2
- 분류: LIS (nlogn), 이분탐색

- 차이점: 값의 범위가 1~100만에서 -10억~10억이 되었기 때문에 lis=[0] 으로 시작하면 안 된다.
"""
