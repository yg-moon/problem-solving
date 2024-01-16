# 문제집
from collections import defaultdict
import sys, heapq

input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)
idg = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    idg[B] += 1


def topo_sort():
    pq = []  # 핵심: 우선순위 큐
    result = []

    for i in range(1, N + 1):
        if idg[i] == 0:
            heapq.heappush(pq, i)

    while pq:
        cur = heapq.heappop(pq)
        result.append(cur)

        for nxt in graph[cur]:
            idg[nxt] -= 1
            if idg[nxt] == 0:
                heapq.heappush(pq, nxt)

    return result


print(*topo_sort())

"""
- 난이도: 골드2
- 분류: 위상정렬 + 우선순위 큐
- 소요 시간: 10분
"""
