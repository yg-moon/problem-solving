# BOJ 1197
import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # 주의: 양방향 간선


def prim():
    start = 1  # 시작점은 어디로 해도 무방
    visited = [False] * (V + 1)  # dist와 별도로 visited가 따로 존재
    dist = [INF] * (V + 1)
    dist[start] = 0
    pq = [(0, start)]
    total_cost = 0

    while pq:
        cur_w, cur = heapq.heappop(pq)

        if visited[cur]:
            continue
        visited[cur] = True
        total_cost += cur_w

        for nxt, nxt_w in graph[cur]:
            if not visited[nxt] and dist[nxt] > nxt_w:
                dist[nxt] = nxt_w
                heapq.heappush(pq, (nxt_w, nxt))

    return total_cost


print(prim())
