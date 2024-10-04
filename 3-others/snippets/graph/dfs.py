from collections import defaultdict

N = 10
graph = defaultdict(list)
visited = [False] * N
result = []


def dfs(cur):
    visited[cur] = True
    result.append(cur)

    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)


def dfs_stack(start):
    stack = [start]

    while stack:
        cur = stack.pop()

        # 현재 노드를 방문처리
        if not visited[cur]:
            visited[cur] = True
            result.append(cur)

            # 연결된 미방문 노드를 스택에 추가
            for nxt in graph[cur]:
                if not visited[nxt]:
                    stack.append(nxt)


"""
- O(V+E)
- 깊은 탐색이 필요할 경우에는 스택 방식이 유리함
"""
