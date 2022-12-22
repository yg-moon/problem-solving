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
        for next in graph[cur]:
            if dist[next] == -1:
                dist[next] = dist[cur] + 1
                q.append(next)

    vals = list(dist.values())
    return vals.count(max(vals))


"""
- 모든 간선의 가중치가 같다면 BFS로 최단경로를 구할 수 있다.
"""
