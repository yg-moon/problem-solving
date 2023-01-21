# 벽 부수고 이동하기
# 출처: https://hongcoding.tistory.com/18
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 핵심: 3차원 배열로 벽의 파괴 여부를 확인
# - visited[x][y][0]은 벽을 파괴하지 않은 상태
# - visited[x][y][1]은 벽을 파괴한 상태
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1


def bfs():
    q = deque([(0, 0, 0)])
    while q:
        x, y, wall = q.popleft()
        if (x, y) == (N - 1, M - 1):
            return visited[x][y][wall]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            # 다음 위치가 벽이고, 아직 벽을 파괴하지 않은 경우: 부수고 이동
            if graph[nx][ny] == 1 and wall == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append((nx, ny, 1))
            # 다음 위치가 길이고, 아직 방문하지 않은 곳인 경우: 그냥 이동
            elif graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                visited[nx][ny][wall] = visited[x][y][wall] + 1
                q.append((nx, ny, wall))
    return -1


print(bfs())

"""
- 난이도: 골드3
- 분류: BFS

요약
- 2층으로 된 공간에서 BFS를 진행한다고 상상하면 된다. (벽을 이미 부순 경우 vs 아직 안 부순 경우)
- BFS로 가까운 곳부터 모든 경우를 시도해보며 진행한다.
    - 벽을 아직 안 부쉈다면, 남은 동안 벽을 부수는 경로도 고려
    - 벽을 이미 부쉈다면, 남은 동안은 길로만 이동

디버깅
- 시간 초과: 모든 벽을 한번씩 부숴가며 최단거리를 구하는 방식으로는 풀 수 없는 문제다.
"""
