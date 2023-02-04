from collections import defaultdict


def solution(tickets):
    # {출발점: [도착점 목록]}
    graph = defaultdict(list)
    for src, dst in sorted(tickets):
        graph[src].append(dst)

    answer = []
    found = False

    def dfs(airport, path):
        # 항공권이 아직 남았는데, 다음 행선지가 없다면 탐색 중단
        if len(path) <= len(tickets) and not graph[airport]:
            return

        # 항공권을 다 사용했고, 다음 행선지가 없다면 가장 먼저 찾은 경로가 정답
        nonlocal answer, found
        if len(path) == len(tickets) + 1 and not graph[airport] and not found:
            answer = path[:]
            found = True
            return

        # 현재 공항에서 갈 수 있는 모든 목적지에 대해 DFS 완전탐색
        for city in graph[airport]:
            # 삭제
            idx = graph[airport].index(city)
            graph[airport].remove(city)
            path.append(city)
            # 재귀
            dfs(city, path)
            # 복구
            path.pop()
            graph[airport].insert(idx, city)

    dfs("ICN", ["ICN"])

    return answer


"""
- DFS 완전탐색
- LeetCode #332: Time Limit Exceeded
"""
