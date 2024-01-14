# LCA
from collections import defaultdict
import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

graph = defaultdict(list)

N = int(input())
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N + 1)
visited = [0] * (N + 1)
depth = [0] * (N + 1)


# 모든 노드의 깊이를 구하기
def dfs(cur, cur_depth):
    visited[cur] = True
    depth[cur] = cur_depth  # 깊이 기록

    for nxt in graph[cur]:
        if not visited[nxt]:
            parent[nxt] = cur  # 부모 기록
            dfs(nxt, cur_depth + 1)


def lca(a, b):
    # 깊이 맞추기
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 공통조상 찾기
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


dfs(1, 0)  # (루트 1, 깊이 0)에서 시작

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))

"""
- 난이도: 골드3
- 분류: 트리

출처
- 코드: https://bbbyung2.tistory.com/75
- 설명: https://konkukcodekat.tistory.com/entry/백준-11437-최소-공통-조상LCA-알고리즘기본-파이썬Python
"""
