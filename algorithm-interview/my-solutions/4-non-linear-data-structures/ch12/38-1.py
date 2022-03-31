import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # {출발점: [도착점 목록]} 으로 구성된 딕셔너리 생성
        for departure, arrival in sorted(tickets):
            graph[departure].append(arrival)

        route = []

        def dfs(airport):
            # 도착점 -> 출발점이 연결되는 곳 찾기
            while graph[airport]:
                dfs(graph[airport].pop(0))
            route.append(airport)

        dfs('JFK')
        # 결과가 거꾸로 된 상태이므로 뒤집기
        return route[::-1]
