from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

# 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    # 큐: 현재 좌표와 count를 함께 저장
    Q = deque([(x, y, 1)])
    # 방문한 곳은 2로 표시
    graph[x][y] = 2
    while Q:
        qx, qy, qcnt = Q.popleft()
        for k in range(4):
            nx = qx + dx[k]
            ny = qy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                # 최적화: 답을 찾으면 즉시 종료
                if nx == N - 1 and ny == M - 1:
                    return qcnt + 1
                graph[qx][qy] = 2
                Q.append((nx, ny, qcnt + 1))
    # 미로의 정답이 없는 경우
    return -1


print(bfs(0, 0))
