import heapq


def solution(n, start, end, roads, traps):
    def is_trap(node):
        if node in traps:
            return True
        return False

    # 그래프 채우기: 인접행렬
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for P, Q, S in roads:
        graph[P][Q] = min(graph[P][Q], S)

    # 다익스트라 변형
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur_w, cur = heapq.heappop(pq)

        if cur == end:
            break

        if dist[cur] < cur_w:
            continue

        # 함정일 경우 화살표 뒤집기
        if is_trap(cur):
            for j in range(1, n + 1):
                graph[cur][j], graph[j][cur] = graph[j][cur], graph[cur][j]

        for nxt in range(1, n + 1):
            nxt_w = graph[cur][nxt]
            if nxt_w != INF:
                new_w = cur_w + nxt_w
                if dist[nxt] > new_w or (is_trap(cur) and is_trap(nxt)):
                    dist[nxt] = new_w
                    heapq.heappush(pq, (new_w, nxt))

    return dist[end]


"""
(틀린 풀이)

- 분류: 다익스트라
- 소요 시간:
    9:30-9:45 (15분) 계획
    12:30-1:00 (30분) 구현
    1:00-2:00 (1시간) 디버깅 (27개중 2개 실패)

디버깅
- 1. "길이 여러개 존재할 수 있다" -> 입력으로 중복 간선도 주어지므로, 최솟값으로 반영
- 2. relaxation 조건을 여러가지로 시도했으나 계속 답이 틀림 -> 애초에 풀이가 잘못됨
"""
