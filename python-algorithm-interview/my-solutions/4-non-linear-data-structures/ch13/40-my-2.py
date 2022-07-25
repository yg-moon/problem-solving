# 우선순위 큐를 이용한 버전
from typing import List
import collections
import heapq
import sys


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프를 인접 리스트로 구성
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # dist: 최단거리 정보를 저장하는 dict
        dist = collections.defaultdict(int)
        for i in range(1, n+1):
            dist[i] = sys.maxsize
        dist[k] = 0

        # 우선순위 큐: 기준점만 가진채로 시작
        Q = [(0, k)]

        # 현재 큐에 같은 노드가 있는지 확인하는 함수
        def nodeExistsInQ(node):
            for pair in Q:
                if pair[1] == node:
                    return True
            return False

        while Q:
            # 최단거리 노드 뽑기
            curr = heapq.heappop(Q)[1]

            # 현재 노드의 모든 이웃에 대해, relax 진행
            for v, w in graph[curr]:
                if dist[v] > dist[curr] + w:
                    dist[v] = dist[curr] + w
                    # 현재 큐에 같은 노드가 없는 경우에만 큐에 추가
                    if not nodeExistsInQ(v):
                        heapq.heappush(Q, (dist[v], v))

        # 도달할 수 없는 노드가 있는지 확인
        if len(dist) == n:
            return -1

        return max(dist.values())


# Time complexity
#

### Note
# 