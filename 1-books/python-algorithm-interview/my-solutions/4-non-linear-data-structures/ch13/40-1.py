import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 그래프: 인접 리스트로 구성
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # 최단경로를 담는 dict
        dist = collections.defaultdict(int)

        # 큐: [(소요 시간, 정점)]
        Q = [(0, K)]

        # 우선순위 큐를 이용, 매번 최단경로를 dist에 삽입.
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 도달할 수 없는 노드가 있는지 확인
        if len(dist) == N:
            return max(dist.values())
        return -1
