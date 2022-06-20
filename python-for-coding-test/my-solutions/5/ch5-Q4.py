import collections

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j):
    # 현재 좌표와 count를 함께 큐에 저장
    q = collections.deque([(i, j, 1)])
    # 방문한 곳은 2로 표시
    graph[i][j] = 2
    while q:
        qi, qj, qcnt = q.popleft()
        for k in range(4):
            ni = qi + dx[k]
            nj = qj + dy[k]
            if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 1:
                if ni == n - 1 and nj == m - 1:
                    return qcnt + 1
                graph[qi][qj] = 2
                q.append((ni, nj, qcnt + 1))
    # 미로의 정답이 없는 경우
    return -1

print(bfs(0, 0))
