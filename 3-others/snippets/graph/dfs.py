def dfs_recursive(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs_recursive(graph, neighbor, visited)


def dfs_stack(graph, start):
    visited = [False] * (len(graph))
    stack = [start]  # 시작 노드를 스택에 넣음

    while stack:
        v = stack.pop()  # 스택에서 노드를 하나 꺼냄
        if not visited[v]:
            visited[v] = True
            print(v, end=" ")

            # 현재 노드와 연결된 미방문 노드들을 스택에 추가
            for neighbor in reversed(graph[v]):
                if not visited[neighbor]:
                    stack.append(neighbor)


"""
- O(V+E)
- 깊은 탐색이 필요할 경우에는 스택 방식이 유리함
"""
