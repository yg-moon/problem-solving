# LeetCode 207
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for want, need in prerequisites:
            graph[want].append(need)

        # 순환 노드: 사이클 판별
        traced = set()
        # 방문 노드: 가지치기 최적화
        visited = set()

        def dfs(x):
            # 사이클 발견
            if x in traced:
                return False
            # 이미 방문했던 노드는 스킵
            if x in visited:
                return True

            # 연결된 모든 노드 방문
            traced.add(x)
            for y in graph[x]:
                if not dfs(y):
                    return False

            # 탐색 종료 후 순환 노드 삭제
            traced.remove(x)
            # 탐색 종료 후 방문 노드 추가
            visited.add(x)
            # 끝까지 문제가 없다면 사이클 없음
            return True

        # 모든 노드에 대해 dfs
        for want in list(graph):
            if not dfs(want):
                return False

        return True
