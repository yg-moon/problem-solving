# 연구소
# 출처1: https://hongcoding.tistory.com/130
# 출처2: https://cotak.tistory.com/14
from collections import deque
from copy import deepcopy

EMPTY = 0
WALL = 1
VIRUS = 2

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0


def bfs():
    global answer
    # 지도 초기화
    new_graph = deepcopy(graph)
    # 바이러스 퍼뜨리기
    q = deque()
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == VIRUS:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and new_graph[nx][ny] == EMPTY:
                new_graph[nx][ny] = VIRUS
                q.append((nx, ny))
    # 점수 계산
    cnt = 0
    for i in range(N):
        cnt += new_graph[i].count(0)
    answer = max(answer, cnt)


# 백트래킹으로 벽을 세우고, 3개 세웠을 때 BFS.
def build_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == EMPTY:
                graph[i][j] = WALL
                build_wall(cnt + 1)
                graph[i][j] = EMPTY


build_wall(0)

print(answer)

"""
버전2
- 탐색: BFS
- 벽 세우기: 백트래킹
- 성능: 3048ms (;;)
    - 벽 세우기를 백트래킹으로 한게 느린 원인인듯.
    - 3중 for문으로 벽의 조합을 구하면 844ms.
"""
