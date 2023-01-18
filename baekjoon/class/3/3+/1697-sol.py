# 숨바꼭질
# 출처: https://chancoding.tistory.com/193
from collections import deque

N, K = map(int, input().split())
MAX = 100001
dist = [0] * MAX


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == K:
            return dist[v]
        for next_v in (v - 1, v + 1, 2 * v):
            if 0 <= next_v < MAX and not dist[next_v]:
                dist[next_v] = dist[v] + 1
                q.append(next_v)


print(bfs(N))


"""
- 이런식의 풀이도 가능하다: 큐에는 위치만 넣고, dist 배열을 따로 만들어서 해결.
"""
