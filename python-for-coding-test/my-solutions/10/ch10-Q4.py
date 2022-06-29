import collections

n = int(input())
graph = collections.defaultdict(list)
idg = collections.defaultdict(int)
val = collections.defaultdict(int)  # 각 노드의 값

# graph, idg, val 채우기
for i in range(1, n + 1):
    time, *prereqs = map(int, input().split())
    for p in prereqs:
        if p != -1:
            graph[p].append(i)
            idg[i] += 1
    val[i] = time


def topoSort():
    result = val.copy()
    Q = collections.deque()

    # 진입간선이 0개인 노드부터 큐에 넣고 시작
    for i in range(1, n + 1):
        if idg[i] == 0:
            Q.append(i)

    while Q:
        curr = Q.popleft()    
        for i in graph[curr]:
            # 핵심: 인접노드result = max(인접노드result, 현재노드result + 인접노드val)
            result[i] = max(result[i], result[curr] + val[i])
            idg[i] -= 1
            if idg[i] == 0:
                Q.append(i)

    for i in range(1, n + 1):
        print(result[i])


topoSort()
