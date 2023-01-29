# 트리의 지름
# 출처: https://kyun2da.github.io/2021/05/04/tree's_diameter/
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])


def dfs(node, cur_w):
    for nxt, nxt_w in graph[node]:
        if dist[nxt] == -1:
            dist[nxt] = cur_w + nxt_w
            dfs(nxt, cur_w + nxt_w)


# 1번 노드에서 가장 먼 곳을 찾는다.
dist = [-1] * (n + 1)
dist[1] = 0
dfs(1, 0)
start = dist.index(max(dist))

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
dist = [-1] * (n + 1)
dist[start] = 0
dfs(start, 0)

print(max(dist))

"""
- 난이도: 골드4
- 분류: 트리
"""
