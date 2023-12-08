# 효율적인 해킹
import sys
from collections import defaultdict, deque

input = sys.stdin.readline  # 주의: 입력이 1만개 이상이면 빠른 입출력

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)  # 주의: 그래프 방향

max_cnt = 1
answer = []


# 핵심: DFS가 아니라 BFS
def bfs(start):
    q = deque()
    q.append(start)
    visited = [False] * (N + 1)
    visited[start] = True
    cnt = 1

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                cnt += 1

    return cnt


# 모든 노드에서 시작해서 연결된 노드의 개수 세기
for i in range(1, N + 1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        answer.clear()
        answer.append(i)
    elif cnt == max_cnt:
        answer.append(i)

print(*answer)

"""
- 난이도: 실버1
- 분류: BFS

- 디버깅: DFS로 하니까 시간초과 -> 입력이 큰 문제에서는 BFS를 사용하자.
"""
