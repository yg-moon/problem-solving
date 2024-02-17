# 도영이가 만든 맛있는 음식
import sys

N = int(input())
min_diff = sys.maxsize
pairs = []

for _ in range(N):
    S, B = map(int, input().split())
    pairs.append((S, B))


def dfs(comb, start):
    global min_diff

    if len(comb) > N:
        return

    if comb:
        s = 1
        b = 0
        for pair in comb:
            s *= pair[0]
            b += pair[1]
        min_diff = min(min_diff, abs(s - b))

    for i in range(start, N):
        comb.append(pairs[i])
        dfs(comb, i + 1)
        comb.pop()


dfs([], 0)

print(min_diff)

"""
- 난이도: 실버2
- 분류: 백트래킹

- 효율은 동일하지만 구현 방법만 다른 풀이
"""
