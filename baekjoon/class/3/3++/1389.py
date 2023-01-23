# 케빈 베이컨의 6단계 법칙
from collections import defaultdict, deque

N, M = map(int, input().split())
graph = defaultdict(list)
result = []  # 사람들의 케빈 베이컨 수

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start, target):
    q = deque([[start, 0]])
    visited = set([start])
    min_dist = int(1e9)
    while q:
        node, dist = q.popleft()
        if node == target:
            min_dist = min(min_dist, dist)
        for next in graph[node]:
            if next not in visited:
                visited.add(next)
                q.append([next, dist + 1])
    return min_dist


for i in range(1, N + 1):
    kb_num = 0
    for j in range(1, N + 1):
        if i != j:
            kb_num += bfs(i, j)
    result.append(kb_num)

print(result.index(min(result)) + 1)

"""
- 난이도: 실버1
- 분류: BFS

- BFS로 모든 쌍 최단거리를 구하는 문제. (플로이드-워셜도 가능)
"""
