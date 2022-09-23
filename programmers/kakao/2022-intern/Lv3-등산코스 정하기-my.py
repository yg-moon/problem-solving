# 시간초과. (다익스트라가 아니라 완전탐색이라서)
from collections import defaultdict


def solution(n, paths, gates, summits):
    min_intensity = int(1e9)
    result = []

    graph = defaultdict(list)
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))

    def dfs(visited, start, curr, intensity):
        nonlocal min_intensity

        if curr != start and curr in gates:
            return

        if curr in summits:
            if min_intensity > intensity:
                min_intensity = intensity
                result.clear()
                result.append(curr)
            if min_intensity == intensity:
                result.append(curr)
            return

        visited.append(curr)

        for v, w in graph[curr]:
            if v not in visited:
                next_intensity = max(intensity, w)
                dfs(visited[:], start, v, next_intensity)

    for g in gates:
        dfs([], g, g, 0)

    return [min(result), min_intensity]


"""
개념
- intensity: 경로 하나의 최대 길이

조건
- 출입구 - 산봉우리(1번만) - 원래 출입구
- 가장 낮은 intensity
- 최소 intensity 코스가 여러개면 가장 낮은 산봉우리

구현
- 각 시작점마다 출발해서, 산봉우리에 도달할 때 까지.
- def dfs (visited, 현재노드, intensity)
-   현재노드가 출발점이면 종료.
-   현재노드가 산봉우리면 종료, 현재까지의 intensity 및 봉우리 기록. (최소일때)
-   현재노드와 연결된 노드들에 대해서 재귀. (visited 제외)
"""
