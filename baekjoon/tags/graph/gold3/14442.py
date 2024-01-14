# 벽 부수고 이동하기 2
from collections import deque

N, M, K = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    q = deque()
    q.append((0, 0, 0))
    # dist[z][x][y]: 벽을 z번 부쉈을때 (x,y) 방문여부 및 거리
    dist = [[[-1] * M for _ in range(N)] for _ in range(K + 1)]
    dist[0][0][0] = 1  # 주의: 이 문제는 시작을 1로 침

    while q:
        x, y, cur_k = q.popleft()

        if x == N - 1 and y == M - 1:
            return dist[cur_k][x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                # 그냥 이동하는 경우
                if graph[nx][ny] == 0 and dist[cur_k][nx][ny] == -1:
                    q.append((nx, ny, cur_k))
                    dist[cur_k][nx][ny] = dist[cur_k][x][y] + 1
                # 벽을 부수는 경우
                elif cur_k < K and graph[nx][ny] == 1 and dist[cur_k + 1][nx][ny] == -1:
                    q.append((nx, ny, cur_k + 1))
                    dist[cur_k + 1][nx][ny] = dist[cur_k][x][y] + 1

    return -1


print(bfs())

"""
- 난이도: 골드3
- 분류: BFS
- 소요 시간: 20분

요약
- #1600(말이 되고픈 원숭이)와 유사한 문제
- 벽을 몇 번 부쉈는지 기록하면서 이동
- 그냥 이동하는 경우와, 벽을 부수는 경우를 구분
"""
