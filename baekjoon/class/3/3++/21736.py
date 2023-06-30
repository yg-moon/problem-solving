# 헌내기는 친구가 필요해
from collections import deque

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "I":
            start_x = i
            start_y = j

# BFS
q = deque()
q.append((start_x, start_y))
visited = [[False] * M for _ in range(N)]
visited[start_x][start_y] = True

while q:
    x, y = q.popleft()
    if graph[x][y] == "P":
        cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 주의: 자꾸 여기서 로직 실수해서 헤맴 (graph[nx][ny] == "O"로 쓰면 안 됨)
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != "X" and not visited[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny] = True

print(cnt if cnt != 0 else "TT")

"""
- 난이도: 실버2
- 분류: BFS
"""
