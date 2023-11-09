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
        cur_w, cur_node = heapq.heappop(pq)
        if dist[cur_node] < cur_w:
            continue
        for nxt_node, nxt_w in graph[cur_node]:
            new_w = cur_w + nxt_w
            if dist[nxt_node] > new_w:
                dist[nxt_node] = new_w
                heapq.heappush(pq, (new_w, nxt_node))
    return dist


result = dijkstra(K)

for i in range(1, V + 1):
    print(result[i] if result[i] != INF else "INF")
