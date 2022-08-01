from collections import defaultdict, deque

N = int(input())
graph = defaultdict(list)
indegree = defaultdict(int)
node_val = defaultdict(int)

# 세 변수 내용 채우기
for i in range(1, N + 1):
    time, *prereqs = map(int, input().split())
    for p in prereqs:
        if p != -1:
            graph[p].append(i)
            indegree[i] += 1
    node_val[i] = time


def topoSort():
    result = node_val.copy()
    Q = deque()

    # 진입차수가 0인 노드부터 큐에 넣고 시작
    for i in range(1, N + 1):
        if indegree[i] == 0:
            Q.append(i)

    while Q:
        curr = Q.popleft()
        for i in graph[curr]:
            # 핵심: 인접노드result = max(인접노드result, 현재노드result + 인접노드val)
            result[i] = max(result[i], result[curr] + node_val[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                Q.append(i)

    for i in range(1, N + 1):
        print(result[i])


topoSort()
