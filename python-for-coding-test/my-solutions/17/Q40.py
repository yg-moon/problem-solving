import heapq
from collections import defaultdict

N, M = map(int, input().split())

# 그래프 구성
graph = defaultdict(list)
for _ in range(M):
    # 모든 간선의 비용은 1 이므로 생략
    u, v = map(int, input().split())
    # 양방향 그래프
    graph[u].append(v)
    graph[v].append(u)

# 다익스트라
# 술래는 항상 1번에서 출발
dist = defaultdict(int)
Q = [(0, 1)]  # [(소요시간, 노드)]
while Q:
    time, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = time
        for v in graph[node]:
            alt = time + 1
            heapq.heappush(Q, (alt, v))

# 결과 추출
values = list(dist.values())
max_len = max(values)
cnt = values.count(max_len)

target = 0
for i in range(1, N + 1):
    if dist[i] == max_len:
        target = i
        break

# (가장 먼 헛간, 그 헛간까지 거리, 그 헛간과 같은 헛간 개수)
print(target, max_len, cnt)
