from collections import defaultdict, deque


def topo_sort(n, graph):
    indegree = [0] * n
    for cur in graph:
        for nxt in graph[cur]:
            indegree[nxt] += 1

    cnt = 0
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        cnt += 1
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    # 핵심2: 위상정렬 이후에도 노드가 남아있다면 사이클이 존재한다는 의미
    return cnt == n


def solution(n, path, order):
    # 양방향 그래프 입력
    graph = defaultdict(list)
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    # 핵심1: 단방향으로 변환
    tmp_q = deque([0])
    while tmp_q:
        cur = tmp_q.popleft()
        for nxt in graph[cur]:
            tmp_q.append(nxt)
            graph[nxt].remove(cur)

    # 우선순위도 그래프에 반영
    for a, b in order:
        graph[a].append(b)

    return topo_sort(n, graph)


"""
- 분류: 그래프 (사이클 판별)
- 위상정렬 풀이
- 참고: https://2jinishappy.tistory.com/200
"""
