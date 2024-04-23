from collections import defaultdict


def solution(info, edges):
    graph = defaultdict(list)
    answer = 0

    for a, b in edges:
        graph[a].append(b)

    def dfs(cur, sheep, wolf, visited):
        nonlocal answer

        # 현재노드의 값을 보고 양과 늑대의 수 갱신
        if info[cur] == 0:
            sheep += 1
        else:
            wolf += 1

        # 늑대 >= 양 이면 종료
        if wolf >= sheep:
            return

        # 양 최대치 갱신
        answer = max(answer, sheep)

        # 현재노드 방문처리
        visited.add(cur)

        # 핵심: 방문한 노드들의 모든 자식들에 대해 재귀
        for node in visited:
            for child in graph[node]:
                # 주의: 이미 방문한 노드는 제외
                if child not in visited:
                    dfs(child, sheep, wolf, visited)

        # 백트래킹을 위해 현재노드의 방문처리는 롤백
        visited.remove(cur)

    dfs(0, 0, 0, set())

    return answer


"""
- 분류: 백트래킹
- 소요 시간: 45분

핵심
- 방문한 노드들의 모든 자식들에 대해 재귀
- 단, 재귀할 노드는 아직 방문한 노드가 아니어야 함
"""
