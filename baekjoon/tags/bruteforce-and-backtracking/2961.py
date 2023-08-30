# 도영이가 만든 맛있는 음식
from itertools import combinations
import sys

N = int(input())
min_diff = sys.maxsize

pairs = []
for _ in range(N):
    S, B = map(int, input().split())
    pairs.append((S, B))

for i in range(1, N + 1):
    for comb in combinations(pairs, i):
        s = 1
        b = 0
        for pair in comb:
            s *= pair[0]
            b += pair[1]
        min_diff = min(min_diff, abs(s - b))

print(min_diff)

"""
- 난이도: 실버2
- 분류: 브루트포스, 백트래킹

- 조합 라이브러리 사용
"""
