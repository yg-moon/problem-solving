# 파알인 버전
# dist를 비어있는 상태로 시작해서, 값이 없는 경우에만 채운다.
# relaxation도 따로 진행하지 않는다.

import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 그래프 구성
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # 최단거리 정보
        dist = collections.defaultdict(int)

        # 큐: [(소요 시간, 노드)]
        Q = [(0, K)]

        # 우선순위 큐를 이용, 매번 최단경로를 삽입.
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 도달할 수 없는 노드 존재여부 확인
        if len(dist) == N:
            return max(dist.values())
        return -1
