from collections import defaultdict
import heapq

N, M, K, X = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    src, dst = map(int, input().split())
    graph[src].append((dst, 1))


def dijkstra(start, target_dist):
    dist = defaultdict(int)
    Q = [(0, start)]
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    answer = []
    for node in dist:
        if dist[node] == target_dist:
            answer.append(node)
    return answer


result = dijkstra(X, K)
if not result:
    print(-1)
else:
    for r in result:
        print(r)
