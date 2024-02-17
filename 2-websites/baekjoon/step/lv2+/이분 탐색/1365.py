# 꼬인 전깃줄
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

lis = []

for a in A:
    idx = bisect_left(lis, a)
    if len(lis) == idx:
        lis.append(a)
    else:
        lis[idx] = a

print(len(A) - len(lis))

"""
- 난이도: 골드2
- 분류: LIS (nlogn)
"""
