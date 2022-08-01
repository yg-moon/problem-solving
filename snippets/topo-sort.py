from collections import deque, defaultdict

V, E = map(int, input().split())
graph = defaultdict(list)  # 인접리스트 그래프
indegree = [0] * (V + 1)  # 진입차수 배열
result = []  # 위상정렬 결과

# 예시 입력
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
# 예시 출력
# 1 2 5 3 6 4 7
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 도착점의 진입차수 +1.
    indegree[b] += 1


def topo_sort():
    Q = deque()
    # 진입차수가 0인 노드를 큐에 넣는다.
    for i in range(1, V + 1):
        if indegree[i] == 0:
            Q.append(i)
    # 큐가 빌 때 까지
    while Q:
        now = Q.popleft()
        # 큐에서 꺼낸 순서가 위상 정렬의 결과.
        result.append(now)
        # 해당 노드에서 출발하는 간선 전부를 그래프에서 제거.
        # 구현: 해당 노드와 연결된 노드들의 진입차수를 -1.
        for i in graph[now]:
            indegree[i] -= 1
            # 다시 진입차수가 0인 노드를 큐에 넣는다.
            if indegree[i] == 0:
                Q.append(i)


topo_sort()

for i in result:
    print(i, end=" ")
print()
