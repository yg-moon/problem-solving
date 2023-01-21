# 트리의 부모 찾기
# 출처: https://yongku.tistory.com/entry/백준-알고리즘-백준-11725번-트리의-부모-찾기-파이썬Python
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(cur):
    # 연결된 노드들에 대해, 부모가 없으면 현재노드를 다음노드의 부모로 설정해주고, 나머지는 DFS
    for nxt in graph[cur]:
        if parent[nxt] == 0:
            parent[nxt] = cur
            dfs(nxt)


dfs(1)

for i in range(2, N + 1):
    print(parent[i])

"""
- 난이도: 실버2
- 분류: DFS/BFS

- DFS 버전 (PyPy로 제출하면 메모리 초과)
- 팁: 트리 DFS 문제는 루트부터 시작해서 같은 로직으로 재귀적으로 돌면 된다.
"""
