# 숨바꼭질 2
# 출처: https://latte-is-horse.tistory.com/338
from collections import deque

N, K = map(int, input().split())
MAX = 100001

q = deque([[N, 0]])
visited = set([N])

ans_time = MAX - 1
ans_way = 0

while q:
    cur, time = q.popleft()
    # 해결책2
    visited.add(cur)
    if time > ans_time:
        continue
    if cur == K:
        ans_time = time
        ans_way += 1
    for nxt in [cur - 1, cur + 1, 2 * cur]:
        if 0 <= nxt < MAX and nxt not in visited:
            q.append([nxt, time + 1])

print(ans_time)
print(ans_way)

"""
- 해결책2: 큐에 넣을 때가 아니라, 큐에서 꺼낼 때 방문처리를 한다. (일단 큐에는 들어갈 수 있게 되므로)
"""
