import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프: 인접 리스트로 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, k)]

        # k step을 넘어가는건 다 버리고, 그 이내에서 결과값이 있으면 리턴.
        while Q:
            price, node, steps_left = heapq.heappop(Q)
            if node == dst:
                return price
            if steps_left >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, steps_left - 1))
        return -1
