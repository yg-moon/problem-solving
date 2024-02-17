# 치즈
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

AIR = 2
melt = []
time = 0


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        graph[x][y] = AIR
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < M
                and (graph[nx][ny] == 0 or graph[nx][ny] == AIR)
                and not visited[nx][ny]
            ):
                q.append((nx, ny))
                visited[nx][ny] = True


while True:
    # 치즈 녹이기
    if melt:
        for x, y in melt:
            graph[x][y] = 0
        melt.clear()

    # 외부공기 전파
    bfs(0, 0)

    # 다음 녹을 치즈 표시
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 1:
                air_cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == AIR:
                        air_cnt += 1
                if air_cnt >= 2:
                    melt.append((x, y))

    # 더 녹을 치즈가 없다면 끝남
    if not melt:
        break

    time += 1

print(time)

"""
- 난이도: 골드3
- 분류: BFS, 시뮬레이션

요약
- (0,0) 에서 BFS 돌려서 닿는데까지 공기로 채우고 시작.
- 주변에 공기가 2개 이상인 치즈는 녹아서 없어짐.
- 다시 (0,0) 에서 BFS 돌려서 공기로 채우고 반복.

다른 풀이: https://it-garden.tistory.com/274
- 그래프의 값을 직접 바꿔서 해결하는 방법도 있다.
"""
