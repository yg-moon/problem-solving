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

result = node_val.copy()


def topoSort():
    Q = deque()
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


topoSort()

for i in range(1, N + 1):
    print(result[i])
