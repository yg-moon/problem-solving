# BOJ 18405
# from 이코테
from collections import deque

N, K = map(int, input().split())

graph = []
virus_info = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            virus_info.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
virus_info.sort()
Q = deque(virus_info)

S, X, Y = map(int, input().split())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
while Q:
    virus, s, x, y = Q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                Q.append((virus, s + 1, nx, ny))

print(graph[X - 1][Y - 1])
