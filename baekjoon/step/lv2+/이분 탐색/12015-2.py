# 가장 긴 증가하는 부분 수열2
# 출처: https://hongcoding.tistory.com/14
# 설명: https://jainn.tistory.com/90
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

lis = [0]

for a in A:
    # 마지막 값보다 크면 append
    if lis[-1] < a:
        lis.append(a)
    # 아니라면 적절한 위치에 이분탐색으로 삽입
    else:
        lis[bisect_left(lis, a)] = a

print(len(lis) - 1)

"""
- bisect 모듈로 더 간단하게 풀기
"""
