# 지름길
from collections import deque

N, D = map(int, input().split())

bypass = []
for _ in range(N):
    start, end, length = map(int, input().split())
    bypass.append((start, end, length))

# dist[i]: i까지 도달하기 위한 최소거리
INF = int(1e9)
dist = [INF] * (D + 1)


def bfs():
    q = deque()
    q.append((0, 0))
    dist[0] = 0

    while q:
        cur, cur_dist = q.popleft()

        # 지름길로 이동
        for start, end, length in bypass:
            nxt_dist = cur_dist + length
            if cur == start and end <= D and nxt_dist < dist[end]:
                dist[end] = nxt_dist
                q.append((end, nxt_dist))

        # 한칸씩 이동
        if cur + 1 <= D and cur_dist + 1 < dist[cur + 1]:
            dist[cur + 1] = cur_dist + 1
            q.append((cur + 1, cur_dist + 1))

    return dist[D]


print(bfs())

"""
- 난이도: 실버1
- 분류: 다익스트라 (라는데 BFS로 해결)
"""
