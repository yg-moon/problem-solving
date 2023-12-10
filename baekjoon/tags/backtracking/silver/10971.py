# 외판원 순회 2
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
min_cost = int(1e9)


def dfs(start, cur, depth, cost):
    global min_cost, visited

    # 핵심: 현재비용 >= 최소비용일 경우 즉시 종료 (pruning)
    if cost >= min_cost:
        return

    if depth == N and cur == start:
        min_cost = min(min_cost, cost)
        return

    for nxt in range(N):
        if not visited[nxt] and mat[cur][nxt] != 0:
            visited[nxt] = True
            dfs(start, nxt, depth + 1, cost + mat[cur][nxt])
            visited[nxt] = False


for i in range(N):
    visited = [False] * N  # 주의: 돌아와야 하기 때문에 시작지점은 방문처리 하지 않음
    dfs(i, i, 0, 0)

print(min_cost)

"""
- 난이도: 실버2
- 분류: 백트래킹

- 핵심: pruning 조건에 따라 실행시간이 크게 차이남
"""
