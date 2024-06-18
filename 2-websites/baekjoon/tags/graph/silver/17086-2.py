from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
answer = 0


def bfs(sx, sy):
    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * M for _ in range(N)]
    visited[sx][sy] = True

    while q:
        x, y, dist = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    return dist + 1
                q.append((nx, ny, dist + 1))
                visited[nx][ny] = True
    return int(1e9)


for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            dist = bfs(i, j)
            answer = max(answer, dist)

print(answer)

"""
비효율적인 풀이
- 모든 빈칸(0)에서 BFS를 돌려 가장 가까운 상어(1)의 거리를 구함
- BFS를 N*M번 실행해야 함
"""
