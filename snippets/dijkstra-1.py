# 이코테 버전
# dist를 무한으로 채우고 시작한다.
# relaxation도 진행한다.

import collections
import heapq
from typing import List
INF = int(1e9)


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 그래프 구성
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # 최단거리 정보
        dist = collections.defaultdict(int)
        for i in range(1, N + 1):
            dist[i] = INF
        dist[K] = 0

        # 큐: [(소요 시간, 노드)]
        Q = [(0, K)]

        # 우선순위 큐를 이용, 가장 가까운 노드 찾기
        while Q:
            time, node = heapq.heappop(Q)
            # 현재 노드가 이미 처리된 적이 있으면 무시
            if dist[node] < time:
                continue
            # relaxation
            for v, w in graph[node]:
                alt = time + w
                if alt < dist[v]:
                    dist[v] = alt
                    heapq.heappush(Q, (alt, v))

        # 도달할 수 없는 노드 존재여부 확인
        if INF in dist.values():
            return -1
        return max(dist.values())
