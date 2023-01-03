# 토마토
from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

q = deque()  # (x좌표, y좌표, 소요일, 현재까지 추가로 익은 개수)
visited = [[0] * M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
answer = -1
target = 0
total_cnt = 0
already = 0

# 초깃값 설정
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            target += 1
        elif graph[i][j] == 1:
            q.append((i, j, 0, 0))
            visited[i][j] = 1
            already += 1

if already == N * M:
    # 이미 모든 토마토가 익어있다면 0을 출력
    print(0)
else:
    # BFS
    while q:
        x, y, day, cur_cnt = q.popleft()
        if cur_cnt == target:
            answer = day
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < M
                and graph[nx][ny] == 0
                and visited[nx][ny] == 0
            ):
                total_cnt += 1
                q.append((nx, ny, day + 1, total_cnt))
                visited[nx][ny] = 1
    print(answer)

"""
- 난이도: 골드5
- 분류: BFS

실행시간 팁
- dx, dy는 처음에 한번만 선언하는게 효율적 (-300ms)
- visited는 set보다 2차원 배열로 관리하는게 효율적 (-1000ms)
"""
