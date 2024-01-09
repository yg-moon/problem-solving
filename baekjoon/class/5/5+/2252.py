# 줄 세우기
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)
indegree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1


def topo_sort():
    q = deque()
    result = []

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        result.append(cur)

        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    return result


print(*topo_sort())

"""
- 난이도: 골드3
- 분류: 위상정렬

- 가장 기본적인 위상정렬
"""
