# 이동하기
import sys

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 1]
dy = [1, 0, 1]

# dp[i][j]: (i,j)에서 '출발'했을때 가능한 최대 사탕개수
dp = [[-1] * M for _ in range(N)]


def dfs(x, y):
    # base case
    if x == N - 1 and y == M - 1:
        return graph[x][y]  # 주의: 여기서 dp[x][y] 라고 쓰면 틀림!

    if dp[x][y] != -1:
        return dp[x][y]

    # 방문표시 및 초기화
    dp[x][y] = 0

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            dp[x][y] = max(dp[x][y], graph[x][y] + dfs(nx, ny))

    return dp[x][y]


print(dfs(0, 0))

"""
- DFS+DP 풀이
"""
