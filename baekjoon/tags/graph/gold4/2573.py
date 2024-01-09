# 빙산
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

time = 0


# 빙산이 1년 녹은 이후의 그래프를 리턴
def get_melted_graph():
    ret = [[0] * M for _ in range(N)]

    for x in range(N):
        for y in range(M):
            sea_cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                    sea_cnt += 1
            ret[x][y] = max(0, graph[x][y] - sea_cnt)

    return ret


# 연결된 덩어리 찾기
def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < M
                and graph[nx][ny] != 0
                and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                q.append((nx, ny))


# 시간에 따라 시뮬레이션
while True:
    visited = [[False] * M for _ in range(N)]
    island_cnt = 0
    ice_sum = 0

    # 덩어리 개수 세기
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and not visited[i][j]:
                bfs(i, j)
                island_cnt += 1
            ice_sum += graph[i][j]

    if island_cnt >= 2:
        break

    # 주의: 이미 전부 녹은 경우도 고려
    if ice_sum == 0:
        time = 0
        break

    # 시간이 흐르고, 얼음이 녹음
    time += 1
    graph = get_melted_graph()

print(time)

"""
- 난이도: 골드4
- 분류: DFS/BFS
- 소요 시간: 20분

요약
- 1년마다 상하좌우에 있는 0의 개수만큼 줄어듦
- 몇 년 후에 덩어리가 2개 이상 되는지 구하기

디버깅: 시간초과
- 1. DFS는 느림 -> 가급적 BFS를 사용
- 2. 다 녹았으면 0을 출력했어야 함 -> while True 쓸때는 무한루프에 주의
"""
