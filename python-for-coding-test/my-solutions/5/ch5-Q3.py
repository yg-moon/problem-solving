n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def dfs(i, j):
    # 칸막이거나 범위를 벗어나면 return
    if i < 0 or i >= n or j < 0 or j >= m or graph[i][j] != 0:
        return
    
    # 방문한 곳 표시
    graph[i][j] = 2

    # 동서남북 재귀
    dfs(i, j+1)
    dfs(i, j-1)
    dfs(i+1, j)
    dfs(i-1, j)

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i, j)
            cnt += 1
print(cnt)
