# 숨바꼭질
# 출처: https://chancoding.tistory.com/193
from collections import deque

MAX = 100001

N, K = map(int, input().split())
dist = [0] * MAX


def bfs(start):
    q = deque([start])
    while q:
        cur = q.popleft()
        if cur == K:
            return dist[cur]
        for nxt in [cur - 1, cur + 1, 2 * cur]:
            if 0 <= nxt < MAX and dist[nxt] == 0:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)


print(bfs(N))


"""
- 이런식의 풀이도 가능하다: 큐에는 위치만 넣고, dist 배열을 따로 만들어서 해결.
"""
