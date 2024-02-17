# 중량제한
from collections import defaultdict, deque
import sys

input = sys.stdin.readline  # 입력이 1만줄 이상이므로

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
factory1, factory2 = map(int, input().split())


# 현재 중량으로 공장1에서 공장2로 이동이 가능한지 확인
def bfs(weight):
    q = deque()
    q.append(factory1)
    visited = [False] * (N + 1)
    visited[factory1] = True

    while q:
        cur = q.popleft()

        if cur == factory2:
            return True

        for nxt, limit in graph[cur]:
            if not visited[nxt] and limit >= weight:
                q.append(nxt)
                visited[nxt] = True

    return False


# 핵심: 파라메트릭 서치
# - 대상: 물품의 중량
# - 기준: 공장1 -> 공장2 도달 가능 여부
l = 1
r = int(1e9)
answer = 0

while l <= r:
    mid = (l + r) // 2
    if bfs(mid):
        answer = mid
        l = mid + 1
    else:
        r = mid - 1

print(answer)

"""
- 난이도: 골드3
- 분류: 이분탐색 + BFS

핵심: 파라메트릭 서치인걸 눈치채는게 중요했던 문제
- 일단 10억을 보면 이분탐색을 떠올리기
- 특정 조건 속에서 f1에서 f2로 도달 가능한지 확인 -> BFS

출처: https://jie0025.tistory.com/212
"""
