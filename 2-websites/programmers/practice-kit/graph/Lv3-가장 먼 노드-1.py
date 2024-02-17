from collections import defaultdict, deque


def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    dist = defaultdict(int)
    for i in range(1, n + 1):
        dist[i] = -1
    dist[1] = 0

    q = deque([1])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    result = list(dist.values())
    return result.count(max(result))


"""
- 모든 간선의 가중치가 같다면 BFS로 최단경로를 구할 수 있다.
"""
