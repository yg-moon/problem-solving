# 최소비용 구하기 2
# 출처: https://velog.io/@yoopark/baekjoon-11779
import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
start_city, end_city = map(int, input().split())

dist = [INF] * (N + 1)
prev = [0] * (N + 1)  # 핵심: 자신의 이전 노드들의 정보를 관리


def dijk(start):
    dist[start] = 0
    pq = [[0, start]]
    while pq:
        time, node = heapq.heappop(pq)
        if dist[node] < time:
            continue
        for v, w in graph[node]:
            alt = time + w
            if dist[v] > alt:
                dist[v] = alt
                prev[v] = node  # 현재노드(node)를 다음노드(v)의 prev로 설정
                heapq.heappush(pq, (alt, v))


dijk(start_city)

# 경로 만들기
path = [end_city]
now = end_city
while now != start_city:  # 꼬리물기로 재귀탐색
    now = prev[now]
    path.append(now)
path.reverse()

# 정답 출력
print(dist[end_city])
print(len(path))
print(" ".join(map(str, path)))

"""
- 난이도: 골드3
- 분류: 다익스트라
"""
