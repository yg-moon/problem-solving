import heapq
from collections import defaultdict

N, D = map(int, input().split())
graph = defaultdict(list)

# 초기화1: 한칸씩 이동하는 경로
for i in range(D):
    graph[i].append((i + 1, 1))

# 초기화2: 지름길로 이동하는 경로
for _ in range(N):
    u, v, w = map(int, input().split())
    if v <= D:  # 팁: 애초에 입력에서 거르기
        graph[u].append((v, w))

INF = int(1e9)
dist = [INF] * (D + 1)


def dijk(start, end):
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

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


print(dijk(0, D))

"""
다익스트라임을 눈치채는게 중요했던 문제
- 기본: 최단거리, 가중치가 양수
- 핵심: 한칸씩 움직이는 경우는 정점을 생성하면 고려됨
"""
