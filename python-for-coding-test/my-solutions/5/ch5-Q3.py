N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]


def dfs(i, j):
    # 1. 범위를 벗어났거나, 빈 곳이 아니라면 return
    if i < 0 or i >= N or j < 0 or j >= M or graph[i][j] != 0:
        return

    # 2. 방문한 곳 표시
    graph[i][j] = 2

    # 3. 동서남북 재귀
    dfs(i, j + 1)
    dfs(i, j - 1)
    dfs(i + 1, j)
    dfs(i - 1, j)


# 모든 칸을 돌면서 빈칸을 만나면 dfs
cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            dfs(i, j)
            cnt += 1

print(cnt)
