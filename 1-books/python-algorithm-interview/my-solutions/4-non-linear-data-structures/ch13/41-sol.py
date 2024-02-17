# 출처: https://github.com/onlybooks/algorithm-interview/issues/104
from collections import defaultdict
from typing import List
import heapq, sys


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        # 인접리스트 그래프 구성
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # 해당 노드를 방문했던 경로의 (price, k)를 저장
        weight = [(sys.maxsize, K)] * n

        # 큐: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, K)]

        # 다익스트라 응용
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    if alt < weight[v][0] or k - 1 >= weight[v][1]:
                        weight[v] = (alt, k - 1)
                        heapq.heappush(Q, (alt, v, k - 1))
        return -1
