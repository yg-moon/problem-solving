# 트리의 지름
# 출처: https://velog.io/@coding_egg/백준-1991번-트리의-지름-python-파이썬
from collections import deque
import sys

input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    info = list(map(int, input().split()))
    for i in range(1, len(info) - 2, 2):
        graph[info[0]].append((info[i], info[i + 1]))  # 주의: info[0]로 해야함.


def bfs(start):
    q = deque([start])
    dist = [-1] * (V + 1)
    dist[start] = 0
    ret = [0, 0]  # [노드, 거리]
    while q:
        cur = q.popleft()
        for nxt, w in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + w
                q.append(nxt)
                if ret[1] < dist[nxt]:
                    ret = nxt, dist[nxt]
    return ret


node, max_dist = bfs(1)  # 1번 노드에서 가장 먼 곳을 찾는다.
_, max_dist = bfs(node)  # 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.

print(max_dist)

"""
- 난이도: 골드2
- 분류: 트리

요약
- 'BOJ #1967 - 트리의 지름'과 풀이법이 동일하다.
    - N의 제한이 1만 vs 10만이라서, 1967번에서는 나이브한 풀이도 가능해서 난이도가 다른것일뿐.
- DFS 버전은 PyPy로 제출하면 메모리 초과.
    - BFS 버전도 배워보자.

디버깅
- 상황: 맞게 푼 것 같은데 예제부터 틀린다.
- 이유: 그래프 입력을 잘못 받았다. 정보가 꼭 정점 순서대로 들어온다는 보장이 없다.
"""
