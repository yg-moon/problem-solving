from collections import defaultdict
import heapq

INF = int(1e9)


def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    dist = defaultdict(int)
    for i in range(1, n + 1):
        dist[i] = INF
    dist[1] = 0

    q = [(0, 1)]  # (소요시간, 정점)
    while q:
        time, node = heapq.heappop(q)
        if dist[node] < time:
            continue
        for v, w in graph[node]:
            alt = dist[node] + w
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(q, (alt, v))

    vals = list(dist.values())
    return vals.count(max(vals))


"""
- 기본적인 다익스트라
"""
