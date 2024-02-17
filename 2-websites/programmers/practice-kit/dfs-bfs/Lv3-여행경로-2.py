from collections import defaultdict, deque


def solution(tickets):
    # {출발점: [도착점 목록]}
    graph = defaultdict(deque)
    for src, dst in sorted(tickets):
        graph[src].append(dst)

    route = []

    # 꼬리 물기
    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].popleft())
        route.append(airport)

    dfs("ICN")

    # 결과가 거꾸로 된 상태이므로 뒤집기
    return route[::-1]


"""
- LeetCode #332
- DFS 꼬리 물기 (재귀 풀이)
"""
