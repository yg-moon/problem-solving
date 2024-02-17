# 녹색 옷 입은 애가 젤다지?
import heapq

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

problem_cnt = 1


def dijkstra(graph):
    # 주의: 초깃값을 0으로 두면 틀림
    pq = [(graph[0][0], 0, 0)]
    dist = [[int(1e9)] * N for _ in range(N)]
    dist[0][0] = graph[0][0]

    while pq:
        cost, x, y = heapq.heappop(pq)

        # 이미 더 작은 경로를 찾았다면 스킵
        if cost > dist[x][y]:
            continue

        # 핵심: 2차원 그래프에서의 다익스트라
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if dist[nx][ny] > cost + graph[nx][ny]:
                    dist[nx][ny] = cost + graph[nx][ny]
                    heapq.heappush(pq, (dist[nx][ny], nx, ny))

    return dist[N - 1][N - 1]


while True:
    N = int(input())
    if N == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = dijkstra(graph)
    print(f"Problem {problem_cnt}: {answer}")
    problem_cnt += 1

"""
- 난이도: 골드4
- 분류: 다익스트라
- 소요 시간: 15분

핵심: 다익스트라임을 깨닫기
- (0,0)에서 (N,M)까지 이동하는데 합이 최소가 되어야 하므로
- 결국 음수가 아닌 가중치를 가진 그래프에서 최단경로를 찾는 문제
"""
