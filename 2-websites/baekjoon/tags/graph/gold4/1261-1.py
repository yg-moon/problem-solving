# 알고스팟
from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# 핵심1: 0-1 BFS (우선순위가 높은 것을 appendleft)
def bfs():
    q = deque()
    q.append((0, 0))
    # 핵심2: 벽을 깬 횟수를 저장
    dist = [[-1] * M for _ in range(N)]
    dist[0][0] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                # 아직 방문한 적이 없을 때
                if dist[nx][ny] == -1:
                    # 벽이 없는 경우: 이전 횟수를 그대로 계승
                    if graph[nx][ny] == 0:
                        dist[nx][ny] = dist[x][y]
                        q.appendleft((nx, ny))
                    # 벽이 있는 경우: 이전 횟수에 +1
                    else:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))

    return dist[N - 1][M - 1]


print(bfs())

"""
- 난이도: 골드4
- 분류: 0-1 BFS

핵심
- 벽을 깬 횟수를 저장 (dist)
- 빈 곳(0)을 우선적으로 돌도록 appendleft, 그 후에 벽(1)을 돌기

- 참고: https://ji-gwang.tistory.com/302
"""
