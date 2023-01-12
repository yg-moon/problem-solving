# 구간 합 구하기 4
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum_val = 0
psum = [0]  # psum[i]: i번째 수 ‘이전’까지 모든 수들의 합.
for a in arr:
    sum_val += a
    psum.append(sum_val)

for _ in range(M):
    i, j = map(int, input().split())
    print(psum[j] - psum[i - 1])  # A의 [L, R]에 대한 구간합: P[R] - P[L-1]

"""
- 난이도: 실버3
- 분류: 누적합

- N개의 수에 대한 M개의 구간합 쿼리
    - 나이브한 방식은 O(NM)
    - prefix sum 기법을 사용하면 O(1)
"""
