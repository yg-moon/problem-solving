import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)


# 핵심2: 그래프에 사이클이 존재하는지 확인 (DFS)
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


def solution(n, path, order):
    global graph, visited, rec_stack

    old_graph = defaultdict(list)
    graph = defaultdict(list)
    graph[0] = []  # 주의: 런타임 에러

    # 양방향 그래프 입력
    for a, b in path:
        old_graph[a].append(b)
        old_graph[b].append(a)

    # 핵심1: 단방향 그래프로 변환 (위상정렬과 반대 방향으로 했는데, 같은 방향이라도 무방)
    q = deque([0])
    seen = set()
    while q:
        parent = q.popleft()
        seen.add(parent)
        for child in old_graph[parent]:
            if child not in seen:
                q.append(child)
                graph[child].append(parent)

    # 우선순위도 그래프에 반영
    for a, b in order:
        graph[b].append(a)

    # 모든 노드에 대해 사이클 확인
    visited = [False] * n
    rec_stack = [False] * n
    for node in graph:
        if not visited[node]:
            if has_cycle(node):
                return False
    return True


"""
- DFS 풀이 (정해)
"""
