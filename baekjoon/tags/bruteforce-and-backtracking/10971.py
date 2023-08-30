# 외판원 순회 2
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
min_cost = int(1e9)


def solve(start, cur, depth, cost):
    global min_cost

    # 핵심: 현재비용 > 최소비용일 경우 즉시 종료 (pruning)
    if cost > min_cost:
        return

    if depth == N and cur == start:
        min_cost = min(min_cost, cost)

    for nxt in range(N):
        if not visited[nxt] and mat[cur][nxt] != 0:
            visited[nxt] = True
            solve(start, nxt, depth + 1, cost + mat[cur][nxt])
            visited[nxt] = False


for i in range(N):
    visited = [False] * N
    solve(i, i, 0, 0)

print(min_cost)

"""
- 난이도: 실버2
- 분류: 브루트포스, 백트래킹

- 배운점: pruning 조건에 따라 실행시간이 크게 차이남
"""
