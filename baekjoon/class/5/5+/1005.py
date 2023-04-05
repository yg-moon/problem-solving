# ACM Craft
from collections import defaultdict, deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 입력 받기
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))  # 1-idx
    graph = defaultdict(list)
    indegree = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1
    W = int(input())

    def topo_sort():
        result = time[:]
        q = deque()
        for i in range(1, N + 1):
            if indegree[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                result[nxt] = max(result[nxt], result[cur] + time[nxt])  # 핵심
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return result[W]

    print(topo_sort())

"""
- 난이도: 골드3
- 분류: 위상정렬

- 대표 유형: 해당 노드까지의 최댓값을 dp로 기록하는 위상정렬
"""
