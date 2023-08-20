# BOJ 1753
import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    dist = [INF] * (V + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cur_wei, cur_node = heapq.heappop(pq)
        if dist[cur_node] < cur_wei:
            continue
        for nxt_node, nxt_wei in graph[cur_node]:
            new_wei = cur_wei + nxt_wei
            if dist[nxt_node] > new_wei:
                dist[nxt_node] = new_wei
                heapq.heappush(pq, (new_wei, nxt_node))
    return dist


result = dijkstra(K)

for i in range(1, V + 1):
    print(result[i] if result[i] != INF else "INF")
