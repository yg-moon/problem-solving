# 도영이가 만든 맛있는 음식
import sys


def dfs(depth, start):
    global comb, comb_len, min_diff

    if depth == comb_len:
        s = 1
        b = 0
        for pair in comb:
            s *= pair[0]
            b += pair[1]
        min_diff = min(min_diff, abs(s - b))
        return

    for i in range(start, N):
        comb.append(pairs[i])
        dfs(depth + 1, i + 1)
        comb.pop()


N = int(input())
pairs = []
comb = []
min_diff = sys.maxsize

for _ in range(N):
    S, B = map(int, input().split())
    pairs.append((S, B))

for i in range(1, N + 1):
    comb_len = i
    dfs(0, 0)

print(min_diff)

"""
- 난이도: 실버2
- 분류: 브루트포스, 백트래킹

- 조합 직접 구현
"""
