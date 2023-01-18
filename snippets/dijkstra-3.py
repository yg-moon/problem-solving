# 가장 무난한 버전
# - 출처: BOJ 1753 (최단경로)
import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijk(start):
    dist = [INF] * (V + 1)
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
    return dist


result = dijk(K)

for i in range(1, V + 1):
    print("INF" if result[i] == INF else result[i])
