import heapq

M, N = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dijkstra():
    # dist[x][y]: (x,y)에 도달하기 위해 부숴야 하는 방의 개수
    dist = [[int(1e9)] * M for _ in range(N)]  # 차이점: INF로 초기화
    dist[0][0] = 0
    pq = [(0, 0, 0)]

    while pq:
        cost, x, y = heapq.heappop(pq)

        # 이미 더 작은 경로를 찾았다면 스킵
        if cost > dist[x][y]:
            continue

        # 핵심: 2차원 그래프에서의 다익스트라
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if dist[nx][ny] > cost + graph[nx][ny]:
                    dist[nx][ny] = cost + graph[nx][ny]
                    heapq.heappush(pq, (dist[nx][ny], nx, ny))

    return dist[N - 1][M - 1]


print(dijkstra())

"""
- 다익스트라 풀이
- 참고: https://ji-gwang.tistory.com/302
"""
