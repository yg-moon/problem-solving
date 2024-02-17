import collections
import heapq

N, M = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(M):
    src, dst = map(int, input().split())
    # 양방향 그래프
    # 모든 간선의 가중치는 1
    graph[src].append([dst, 1])
    graph[dst].append([src, 1])

X, K = map(int, input().split())


def dijkstra(graph, src, dst):
    dist = collections.defaultdict(int)
    Q = [(0, src)]
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    if len(dist) != N:
        return -1
    return dist[dst]


# A는 1->K->X 순으로 이동
path1 = dijkstra(graph, 1, K)
path2 = dijkstra(graph, K, X)

if path1 == -1 or path2 == -1:
    print(-1)
else:
    print(path1 + path2)
