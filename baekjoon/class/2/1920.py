# 수 찾기
from bisect import bisect_left

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for x in arr2:
    idx = bisect_left(arr1, x)
    if idx < N and arr1[idx] == x:  # 주의: 항상 범위를 벗어나지 않는지 확인 필요
        print(1)
    else:
        print(0)

"""
- 난이도: 실버4
- 분류: 이분탐색
"""
