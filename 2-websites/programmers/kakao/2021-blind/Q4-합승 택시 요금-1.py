from collections import defaultdict
import heapq

N = 0
INF = int(1e9)
graph = defaultdict(list)


def dijk(start, end):
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur_w, cur = heapq.heappop(pq)

        if dist[cur] < cur_w:
            continue

        for nxt, nxt_w in graph[cur]:
            new_w = cur_w + nxt_w
            if dist[nxt] > new_w:
                dist[nxt] = new_w
                heapq.heappush(pq, (new_w, nxt))

    return dist[end]


def solution(n, s, a, b, fares):
    global N, graph
    N = n
    answer = INF

    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))

    for x in range(1, N + 1):
        answer = min(answer, dijk(s, x) + dijk(x, a) + dijk(x, b))

    return answer


"""
- 분류: 최단거리

핵심
- (S -> x) + (x -> A) + (x -> B)가 최소가 되는 경유지 x를 찾기
- 다익스트라 풀이 (O(ElogV))
"""
