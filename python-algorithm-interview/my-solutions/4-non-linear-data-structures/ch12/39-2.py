import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(x):
            # 순환 구조 발견 
            if x in traced:
                return False
            # 이미 방문했던 노드이므로 스킵
            if x in visited:
                return True

            traced.add(x)
            for y in graph[x]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(x)
            # 탐색 종료 후 방문 노드 추가
            visited.add(x)

            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True
