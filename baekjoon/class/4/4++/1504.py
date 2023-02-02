# 특정한 최단 경로
import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))  # 주의: 이번 문제는 양방향
v1, v2 = map(int, input().split())

# 시작점과 도착점이 있는 다익스트라
def dijk(start, end):
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        time, node = heapq.heappop(pq)
        if dist[node] < time:
            continue
        for v, w in graph[node]:
            alt = time + w
            if dist[v] > alt:
                dist[v] = alt
                heapq.heappush(pq, (alt, v))
    return dist[end]


# 핵심: 두개의 후보중 최단경로를 고르기
path1 = dijk(1, v1) + dijk(v1, v2) + dijk(v2, N)
path2 = dijk(1, v2) + dijk(v2, v1) + dijk(v1, N)
result = min(path1, path2)
print(result if result < INF else -1)

"""
- 난이도: 골드4
- 분류: 다익스트라
"""
