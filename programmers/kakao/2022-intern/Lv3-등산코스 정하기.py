# 출처: https://hz25.tistory.com/6
from collections import defaultdict
from heapq import heappop, heappush

INF = int(1e9)


def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))

    PQ = []  # (intensity, 현재 위치)
    dist = [INF] * (n + 1)
    summits_set = set(summits)

    # 모든 출발지를 우선순위 큐에 삽입
    for gate in gates:
        heappush(PQ, (0, gate))
        dist[gate] = 0

    # 다익스트라 변형
    while PQ:
        intensity, node = heappop(PQ)
        # 산봉우리이거나 더 큰 intensity라면 더 이상 이동하지 않음
        if node in summits_set or intensity > dist[node]:
            continue
        for v, w in graph[node]:
            # 다음 위치에 더 작은 intensity로 도착할 수 있다면 갱신
            # 참고: 출입구는 이미 0으로 세팅되어 있기 때문에 방문하지 않음
            new_intensity = max(intensity, w)
            if dist[v] > new_intensity:
                dist[v] = new_intensity
                heappush(PQ, (new_intensity, v))

    # 정답: intensity 값이 가장 작으면서, 동시에 번호가 가장 낮은 산봉우리.
    answer = [0, INF]
    summits.sort()
    for summit in summits:
        if dist[summit] < answer[1]:
            answer[0] = summit
            answer[1] = dist[summit]
    return answer
