import collections
import heapq

n, m, c = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(m):
    src, dst, time = map(int, input().split())
    graph[src].append((dst, time))


def dijkstra(src):
    dist = collections.defaultdict(int)
    Q = [(0, src)]
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
    # 메시지를 받는 총 도시의 갯수 (시작노드 제외)
    cnt = len(dist) - 1
    # 메시지를 받는데 걸리는 총 시간
    longest_time = max(dist.values())
    return [cnt, longest_time]


result = dijkstra(c)
print(result[0], result[1])
