# 내리막 길
# 출처1: https://studyandwrite.tistory.com/387
# 출처2: https://fre2-dom.tistory.com/251
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# dp[i][j]: (i,j)에서 출발하여 목적지까지 도착하는 경로의 개수
dp = [[-1] * N for _ in range(M)]


def dfs(x, y):
    # 목적지에 도착하면 1을 리턴 (효과: 이동한 모든 경로칸에 1을 더함)
    if (x, y) == (M - 1, N - 1):
        return 1

    # 이미 방문한 적이 있다면, 그 위치의 dp값을 리턴 (Top-down)
    if dp[x][y] != -1:
        return dp[x][y]

    # 아직 방문한 적이 없다면, 방문표시 이후 DFS탐색
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[x][y] > graph[nx][ny]:
            # 현재 dp값: 상하좌우로 탐색해서 구한 모든 경로들의 합
            dp[x][y] += dfs(nx, ny)

    # 최종적으로는 시작점의 dp값을 출력하여 모든 경로의 개수를 확인
    return dp[x][y]


print(dfs(0, 0))

"""
- 난이도: 골드3
- 분류: dp

- 유형: DFS + dp (Top-down)
"""
