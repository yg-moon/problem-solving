# 미확인 도착지
from collections import defaultdict
import heapq, sys

input = sys.stdin.readline
INF = int(1e9)


def dijk(start):
    global n
    pq = [(0, start)]
    dist = [INF] * (n + 1)
    dist[start] = 0  # 주의: 시작점 설정 잊지 말기!
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


T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    dests = [int(input()) for _ in range(t)]

    dist_s = dijk(s)
    dist_g = dijk(g)
    dist_h = dijk(h)
    result = []

    # 핵심
    for d in dests:
        if (
            dist_s[g] + dist_g[h] + dist_h[d] == dist_s[d]
            or dist_s[h] + dist_h[g] + dist_g[d] == dist_s[d]
        ):
            result.append(d)

    print(*sorted(result))

"""
- 난이도: 골드2
- 분류: 다익스트라

핵심
- (출발 -> g -> h -> 도착) 혹은
  (출발 -> h -> g -> 도착) 중에서
  (출발 -> 도착) 과 거리가 같다면 해당 도착지점을 정답에 저장.
"""
