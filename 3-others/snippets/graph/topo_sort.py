# BOJ 2252
from collections import deque, defaultdict

V, E = map(int, input().split())
graph = defaultdict(list)
indegree = [0] * (V + 1)
result = []

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 도착점의 진입차수 +1
    indegree[b] += 1


def topo_sort():
    q = deque()
    # 진입차수가 0인 노드를 큐에 넣고 시작
    for i in range(1, V + 1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 다음을 반복
    while q:
        cur = q.popleft()
        # 큐에서 꺼낸 순서가 위상정렬의 결과
        result.append(cur)
        # 큐에서 원소를 꺼내, 해당 노드에서 출발하는 모든 간선을 그래프에서 제거
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            # 다시 진입차수가 0인 노드를 큐에 넣음
            if indegree[nxt] == 0:
                q.append(nxt)


topo_sort()

print(*result)
