# 욕심쟁이 판다
import sys

sys.setrecursionlimit(10**6)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# dp[i][j]: (i,j)에서 출발했을때 이동할 수 있는 최대칸수
dp = [[-1] * N for _ in range(N)]


def dfs(x, y):
    # Top-down: 이미 방문한 곳은 리턴
    if dp[x][y] != -1:
        return dp[x][y]

    # 핵심1(방문표시 및 기본값): 일단 한칸은 가능
    dp[x][y] = 1

    # 핵심2(점화식): 상하좌우에 대해 '다음 위치의 dp값 + 1'중 최댓값을 선택
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > graph[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i, j))
print(answer)

"""
- 난이도: 골드3
- 분류: DFS+DP
- 소요 시간: 45분 (1차 30분, 2차 15분)
"""
