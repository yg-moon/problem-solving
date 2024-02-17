from collections import defaultdict


# 현재 노드에서 출발하여 사이클이 존재하는지 확인 (DFS)
def has_cycle(node):
    global graph, visited, rec_stack

    visited[node] = True
    rec_stack[node] = True

    for nxt in graph[node]:
        if not visited[nxt]:
            if has_cycle(nxt):
                return True
        elif rec_stack[nxt]:
            return True

    rec_stack[node] = False
    return False


# 모든 노드에 대해 사이클 확인
def main(n, edges):
    global graph, visited, rec_stack

    graph = defaultdict(list)
    visited = [False] * n
    rec_stack = [False] * n

    for a, b in edges:
        graph[a].append(b)  # 주의: 그래프는 단방향이어야 함

    for node in graph:
        if not visited[node]:
            if has_cycle(node):
                return False
    return True
