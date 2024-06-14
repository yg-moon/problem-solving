# 친구
from collections import defaultdict, deque

graph = defaultdict(list)

N = int(input())
for i in range(N):
    row = input()
    for j in range(N):
        if row[j] == "Y":
            graph[i].append(j)


# 거리가 2 이내인 모든 친구를 찾기
def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [False] * N
    visited[start] = True
    friends = 0
    while q:
        cur, cnt = q.popleft()
        if cnt >= 2:
            break
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                friends += 1
                q.append((nxt, cnt + 1))
    return friends


# 모든 노드에서 출발
max_friends = 0
for i in range(N):
    friends = bfs(i)
    max_friends = max(max_friends, friends)

print(max_friends)

"""
- 난이도: 실버2
- 분류: 그래프, 브루트포스

핵심
- 그래프로 바꾸어 푼다는 발상이 핵심
- 거리가 2만큼 떨어진 모든 사람들이 친구

디버깅: 틀렸습니다
- 이유: DFS로는 못푸는 예외가 존재 (0-1-2-3, 0-2-3로 연결된 경우, 3은 도달 불가)
"""
