# 쉬운 최단거리
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
res = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 참고: one-pass(입력 받으면서 동시에 처리)해도 큰 차이는 없음
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i, j
        elif graph[i][j] == 0:
            res[i][j] = 0

# BFS
visited = [[False] * m for _ in range(n)]
visited[start_x][start_y] = True  # 주의: 시작위치 방문표시하기
q = deque()
q.append((start_x, start_y, 0))
while q:
    cur_x, cur_y, dist = q.popleft()
    res[cur_x][cur_y] = dist
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
            visited[nx][ny] = True
            q.append((nx, ny, dist + 1))

for row in res:
    print(*row)

"""
- 난이도: 실버1
- 분류: BFS

- 헤맨 곳: 시간초과
- 원인: 곧이 곧대로 모든 지점에서 시작해서 '2'를 찾을 때까지 BFS를 한 것이 문제
- 해결: 반대로 생각하기. '2'에서 출발해서 BFS를 하며 이동거리를 기록하면 시간내로 해결 가능
"""
