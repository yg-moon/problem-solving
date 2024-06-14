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


def dijk(start):
    dist = [INF] * (V + 1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_w, cur = heapq.heappop(pq)

        if dist[cur] < cur_w:
            continue

        for nxt, nxt_w in graph[cur]:
            new_w = cur_w + nxt_w
            if dist[nxt] > new_w:
                dist[nxt] = new_w
                heapq.heappush(pq, (new_w, nxt))

    return dist


result = dijk(K)

for i in range(1, V + 1):
    if result[i] != INF:
        print(result[i])
    else:
        print("INF")
