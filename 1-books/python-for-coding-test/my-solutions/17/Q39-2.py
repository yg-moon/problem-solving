# - dist 타입: list
# - 이코테 로직
import heapq

INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []

T = int(input())
for _ in range(T):
    N = int(input())
    # Adjacent Matrix (인접 행렬) 그래프
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    # 다익스트라
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = graph[0][0]  # 주의: dist[0][0] = 0 이 아님!
    Q = [(graph[0][0], 0, 0)]

    while Q:
        time, x, y = heapq.heappop(Q)
        if dist[x][y] < time:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                alt = time + graph[nx][ny]
                if alt < dist[nx][ny]:
                    dist[nx][ny] = alt
                    heapq.heappush(Q, (alt, nx, ny))

    answer.append(dist[N - 1][N - 1])

for a in answer:
    print(a)
