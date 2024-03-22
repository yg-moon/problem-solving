from collections import defaultdict, deque


def solution(edges):
    N = 0
    idg = defaultdict(int)
    odg = defaultdict(int)
    graph = defaultdict(list)
    stick_set = set()  # 효율성: 막대 노드는 따로 구분

    for a, b in edges:
        odg[a] += 1
        idg[b] += 1
        graph[a].append(b)
        N = max(N, a, b)

    created = 0
    g1 = 0
    g2 = 0
    g3 = 0
    total = 0
    visited = [False] * (N + 1)

    # 생성된 정점
    for key in odg:
        if idg[key] == 0 and odg[key] >= 2:
            created = key
            total = odg[key]
            break

    # 생성된 정점과 연결된 간선을 삭제
    for a, b in edges:
        if a == created:
            odg[a] -= 1
            idg[b] -= 1
            graph[a].clear()

    # start 노드에서 출발하여 node_set, edge_set을 채움
    def bfs(start):
        q = deque()
        q.append(start)
        while q:
            cur = q.popleft()
            node_set.add(cur)
            for nxt in graph[cur]:
                if nxt not in stick_set and (cur, nxt) not in edge_set:
                    edge_set.add((cur, nxt))
                    if not visited[nxt]:
                        q.append(nxt)

    # 방문하지 않은 모든 노드에 대해 순회
    for i in range(1, N + 1):
        if not visited[i] and i != created:
            node_set = set()
            edge_set = set()
            bfs(i)
            node_cnt = len(node_set)
            edge_cnt = len(edge_set)
            is_stick = True

            if node_cnt == edge_cnt:
                g1 += 1
                is_stick = False
            elif node_cnt + 1 == edge_cnt:
                g3 += 1
                is_stick = False

            if is_stick:
                for node in node_set:
                    stick_set.add(node)
            else:
                for node in node_set:
                    visited[node] = True

    g2 = total - g1 - g3

    return [created, g1, g2, g3]


"""
순회 풀이
- 순회로도 풀 수는 있음
- 다만 순회하더라도 일단 생성된 정점을 제거하는 것이 중요했음
- BFS가 DFS보다 약간 더 빠름
"""
