# 물통
A, B, C = map(int, input().split())
result = []
seen = set()


def dfs(a, b, c):
    if (a, b, c) in seen:
        return

    if a == 0:
        result.append(c)

    seen.add((a, b, c))

    # A -> B
    # A -> C
    if a > 0:
        # 핵심1: 넘겨줄 수 있는만큼만 넘기고 받기
        # 핵심2: min, max 사용해서 범위 유지하기
        dfs(max(0, a - (min(b + a, B) - b)), min(b + a, B), c)
        dfs(max(0, a - (min(c + a, C) - c)), b, min(c + a, C))

    # B -> A
    # B -> C
    if b > 0:
        dfs(min(a + b, A), max(0, b - (min(a + b, A) - a)), c)
        dfs(a, max(0, b - (min(c + b, C) - c)), min(c + b, C))

    # C -> A
    # C -> B
    if c > 0:
        dfs(min(a + c, A), b, max(0, c - (min(a + c, A) - a)))
        dfs(a, min(b + c, B), max(0, c - (min(b + c, B) - b)))


dfs(0, 0, C)

print(*sorted(result))

"""
- 난이도: 골드5
- 분류: DFS/BFS
- 소요 시간: 25분

- DFS 풀이
"""
