# 다리 만들기
from collections import deque

INF = int(1e9)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# 현재 섬을 num으로 색칠하는 함수
def color_island(sx, sy, num):
    q = deque()
    q.append((sx, sy))
    graph[sx][sy] = num

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = num
                q.append((nx, ny))


# 각 섬을 num으로 색칠
num = 2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            color_island(i, j, num)
            num += 1


# 다른 섬까지의 최단거리를 찾는 함수
def find_dist(num):
    q = deque()
    dist = [[-1] * N for _ in range(N)]

    # 최적화: 섬의 좌표들을 시작지점으로 한번에 넣기
    for i in range(N):
        for j in range(N):
            if graph[i][j] == num:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()

        if graph[x][y] != 0 and graph[x][y] != num:
            return dist[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 주의: 항상 방문여부 확인하기!
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

    return INF


# 모든 섬에 대해, 다른 섬으로 가는 최솟값 구하기
answer = INF
for i in range(2, num + 1):
    answer = min(answer, find_dist(i))
print(answer - 1)

"""
- 난이도: 골드3
- 분류: BFS
- 소요 시간: 35분 (풀이 25분, 디버깅 10분)

요약
- 각 섬을 2,3,4...로 넘버링
- 각 섬의 모든 점에서 출발하여, 다른 섬까지 BFS로 도달할때 최단거리중 최솟값을 구하기

디버깅: 메모리 초과
- visited 여부를 확인하지 않았던 것이 문제

최적화
- 목표: 모든 점에서 bfs를 실행하지 말고, 각 섬의 번호마다 한번씩만 실행하기
- 방법: 해당 좌표들을 시작지점으로 한번에 넣기
"""
