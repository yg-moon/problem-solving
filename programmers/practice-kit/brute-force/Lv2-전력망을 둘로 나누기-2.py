def dfs(cur, visited):
    global cnt
    visited.add(cur)
    cnt += 1
    for i in tree[cur]:
        if i not in visited:
            dfs(i, visited)


def solution(n, wires):
    global tree, cnt
    tree = [[] for _ in range(n + 1)]
    answer = int(1e9)

    # 그래프 구축
    for x, y in wires:
        tree[x].append(y)
        tree[y].append(x)

    # 하나씩 끊어보며 DFS
    for x, y in wires:
        # 전선 끊기
        tree[x].remove(y)
        tree[y].remove(x)

        # 아무 노드나 시작점으로 해서 DFS
        cnt = 0
        dfs(1, set())
        answer = min(answer, abs(cnt - (n - cnt)))

        # 전선 복구
        tree[x].append(y)
        tree[y].append(x)

    return answer


"""
- DFS섬 만들기
"""
