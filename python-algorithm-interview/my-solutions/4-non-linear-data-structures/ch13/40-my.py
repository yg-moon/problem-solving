# 다익스트라를 정석대로 구현한 버전
from typing import List
import collections
import sys


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프를 인접 리스트로 구성
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # dist: 최단거리 정보를 저장하는 dict
        dist = collections.defaultdict(int)
        for i in range(1, n + 1):
            dist[i] = sys.maxsize
        dist[k] = 0

        # 모든 노드를 unvisited에 넣고 시작
        unvisited = set()
        for i in range(1, n + 1):
            unvisited.add(i)

        # 출발점과 거리가 가장 가까운 노드를 찾는 함수
        def minDistance():
            min = sys.maxsize
            min_idx = -1
            for i in range(1, n + 1):
                if dist[i] < min and i in unvisited:
                    min = dist[i]
                    min_idx = i
            return min_idx

        # 모든 노드가 방문될 때까지 진행
        while unvisited:
            curr = minDistance()
            # 도달할 수 없는 노드가 있는 경우
            if curr == -1:
                return -1

            unvisited.remove(curr)

            # 현재 노드의 모든 이웃에 대해, relaxation 진행
            for v, w in graph[curr]:
                if dist[v] > dist[curr] + w:
                    dist[v] = dist[curr] + w

        return max(dist.values())
