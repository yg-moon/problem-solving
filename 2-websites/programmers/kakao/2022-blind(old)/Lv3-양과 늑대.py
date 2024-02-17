from collections import defaultdict


def solution(info, edges):
    # {노드 번호: [자식들 번호]}
    children = defaultdict(list)
    for e in edges:
        children[e[0]].append(e[1])

    max_sheep = 0

    def dfs(visited, curr, sheep, wolf):
        # 현재노드의 값을 보고 양과 늑대의 수 갱신
        if info[curr] == 0:
            sheep += 1
        else:
            wolf += 1

        # 늑대 >= 양 이면 종료
        if wolf >= sheep:
            return

        # 양 최대치 갱신
        nonlocal max_sheep
        max_sheep = max(max_sheep, sheep)

        # 현재노드 방문처리
        visited.append(curr)

        # 방문노드들의 모든 자식들에 대해 재귀
        for node in visited:
            for child in children[node]:
                # 주의: 방문노드에 있는 노드들은 제외. 무한루프가 된다
                if child not in visited:
                    dfs(visited[:], child, sheep, wolf)

    dfs([], 0, 0, 0)
    return max_sheep
