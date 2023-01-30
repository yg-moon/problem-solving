# 숨바꼭질 3
# 출처: https://jshong1125.tistory.com/29
from collections import deque

MAX = 100001

N, K = map(int, input().split())
q = deque([N])
visited = [-1 for _ in range(MAX)]
visited[N] = 0

while q:
    s = q.popleft()
    if s == K:
        print(visited[s])
        break
    if 0 <= s * 2 < MAX and visited[s * 2] == -1:
        visited[s * 2] = visited[s]
        q.appendleft(s * 2)  # 2*s 가 다른 연산보다 더 높은 우선순위를 가지기 위함
    if 0 <= s - 1 < MAX and visited[s - 1] == -1:
        visited[s - 1] = visited[s] + 1
        q.append(s - 1)
    if 0 <= s + 1 < 100001 and visited[s + 1] == -1:
        visited[s + 1] = visited[s] + 1
        q.append(s + 1)

"""
- 0-1 BFS 풀이 (appendleft)
"""
