# 가장 긴 증가하는 부분 수열2
# 출처: https://hongcoding.tistory.com/14
# 설명: https://jainn.tistory.com/90
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
LIS = [0]

for a in A:
    # 마지막 값보다 크면 append
    if LIS[-1] < a:
        LIS.append(a)
    # 아니라면 적절한 위치에 이분탐색으로 삽입
    else:
        LIS[bisect_left(LIS, a)] = a

print(len(LIS) - 1)

"""
- bisect 모듈로 더 간단하게 풀기
"""
