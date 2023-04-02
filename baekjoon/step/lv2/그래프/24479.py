# 알고리즘 수업 - 깊이 우선 탐색 1
from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

graph = defaultdict(list)

N, M, R = map(int, input().split())
for _ in range(M):
    u, v = map(int, input().split())
    # 양방향 그래프
    graph[u].append(v)
    graph[v].append(u)

# 오름차순으로 정렬
for key in graph:
    graph[key].sort()

# 방문순서를 기록
visited = [-1] * (N + 1)

# 방문순서는 전역변수로 관리
cnt = 1


def dfs(x):
    global cnt
    visited[x] = cnt
    for nxt in graph[x]:
        if visited[nxt] == -1:
            cnt += 1
            dfs(nxt)


dfs(R)

# 정점 i의 방문순서를 출력
for i in range(1, N + 1):
    if visited[i] != -1:
        print(visited[i])
    else:
        print(0)

"""
- 난이도: 실버2
- 분류: DFS

핵심
- 정점을 오름차순으로 방문하므로, 그래프의 각 인접리스트를 정렬해야 함
- 방문순서를 알아야 하므로, visited는 list로 관리해야 함
- 방문순서(cnt)는 전역변수로 설정해야 함
"""
