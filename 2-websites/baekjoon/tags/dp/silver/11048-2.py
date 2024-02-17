import sys

sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: (i,j)에서 출발했을때 가능한 최대 사탕개수
dp = [[-1] * M for _ in range(N)]


def dfs(x, y):
    # base case
    if x >= N or y >= M:
        return 0

    # top-down
    if dp[x][y] != -1:
        return dp[x][y]

    # 점화식
    dp[x][y] = max(dp[x][y], graph[x][y] + dfs(x + 1, y))
    dp[x][y] = max(dp[x][y], graph[x][y] + dfs(x, y + 1))
    dp[x][y] = max(dp[x][y], graph[x][y] + dfs(x + 1, y + 1))

    return dp[x][y]


print(dfs(0, 0))

"""
- 탑다운 풀이
"""
