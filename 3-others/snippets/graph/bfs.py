from collections import deque, defaultdict

N = 10
graph = defaultdict(list)
visited = [False] * N
result = []


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True  # 주의: 항상 시작노드 방문처리

    while q:
        cur = q.popleft()
        result.append(cur)

        for nxt in graph[cur]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True


"""
- O(V+E)
"""
