# 트리의 부모 찾기
# 출처: https://d-cron.tistory.com/22
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs():
    q = deque([1])
    while q:
        cur = q.popleft()
        # 연결된 노드들에 대해, 부모가 없으면 현재노드를 다음노드의 부모로 설정해주고, 다음노드를 큐에 추가
        for nxt in graph[cur]:
            if parent[nxt] == 0:
                parent[nxt] = cur
                q.append(nxt)


bfs()

for i in range(2, N + 1):
    print(parent[i])

"""
- BFS 버전
- 이 문제는 두가지 방법 다 가능하다.
"""
