from collections import defaultdict


def solution(tickets):
    src_to_dst = defaultdict(list)
    for src, dst in sorted(tickets):
        src_to_dst[src].append(dst)

    answer = []
    found = False

    def dfs(airport, path):
        # 항공권이 아직 남았는데, 다음 행선지가 없다면 탐색 중단
        if len(path) < len(tickets) + 1 and not src_to_dst[airport]:
            return

        # 항공권을 다 사용했고, 다음 행선지가 없다면 처음 찾은 경로가 정답
        nonlocal answer, found
        if len(path) == len(tickets) + 1 and not src_to_dst[airport] and not found:
            answer = path[:]
            found = True
            return

        # 현재 공항에서 갈 수 있는 모든 목적지에 대해 DFS 완전탐색
        for city in src_to_dst[airport]:
            # 삭제
            idx = src_to_dst[airport].index(city)
            src_to_dst[airport].remove(city)
            path.append(city)
            # 재귀
            dfs(city, path)
            # 복구
            path.pop()
            src_to_dst[airport].insert(idx, city)

    dfs("ICN", ["ICN"])
    return answer


"""
- LeetCode #332: Time Limit Exceeded
- DFS 완전탐색
"""
