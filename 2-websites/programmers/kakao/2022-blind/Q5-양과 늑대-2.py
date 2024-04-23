from collections import defaultdict


def solution(info, edges):
    graph = defaultdict(list)
    answer = 0

    for a, b in edges:
        graph[a].append(b)

    def dfs(cur, sheep, wolf, can_visit):
        nonlocal answer

        if info[cur] == 0:
            sheep += 1
        else:
            wolf += 1

        if wolf >= sheep:
            return

        answer = max(answer, sheep)

        # 현재 자식들을 방문 가능한 노드에 추가
        tmp = set()
        for nxt in graph[cur]:
            can_visit.add(nxt)
            tmp.add(nxt)

        # 다음 방문할 노드는, 방문 가능한 노드에서 삭제하고 진행
        for node in list(can_visit):
            can_visit.remove(node)
            dfs(node, sheep, wolf, can_visit)
            can_visit.add(node)

        # 백트래킹을 위해 이번에 추가한 노드는 다시 삭제
        for node in tmp:
            can_visit.remove(node)

    dfs(0, 0, 0, set())

    return answer


"""
- 해설: '다음으로 방문할 수 있는 노드'를 관리
"""
