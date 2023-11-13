from collections import defaultdict
import heapq


def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    INF = int(1e9)
    dist = [INF] * (n + 1)
    pq = []
    summits_set = set(summits)

    # 시간초과 해결: 모든 출입구를 시작점으로 넣고 실행
    for gate in gates:
        heapq.heappush(pq, (0, gate))
        dist[gate] = 0

    # 다익스트라
    while pq:
        cur_w, cur = heapq.heappop(pq)
        # 조건 추가: 산봉우리에 도달했으면 종료
        if dist[cur] < cur_w or cur in summits_set:
            continue
        for nxt, nxt_w in graph[cur]:
            new_w = max(cur_w, nxt_w)
            if dist[nxt] > new_w:
                dist[nxt] = new_w
                heapq.heappush(pq, (new_w, nxt))

    # 답: intensity 값이 가장 작으면서, 동시에 번호가 가장 낮은 산봉우리
    answer = [0, INF]
    summits.sort()
    for summit in summits:
        if dist[summit] < answer[1]:
            answer[0] = summit
            answer[1] = dist[summit]
    return answer


"""
- 다익스트라 풀이 (정해)
"""
