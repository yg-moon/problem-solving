# 물통
from collections import deque

A, B, C = map(int, input().split())

q = deque()
q.append((0, 0))
visited = [[False] * (B + 1) for _ in range(A + 1)]
visited[0][0] = True
result = []


# cup1 -> cup2 으로 물을 붓고 기록을 저장
def pour(cup1, cup2):
    if not visited[cup1][cup2]:
        visited[cup1][cup2] = True
        q.append((cup1, cup2))


def bfs():
    while q:
        a, b = q.popleft()
        c = C - a - b  # a,b가 결정되면 c는 유일하다는 것을 이용

        if a == 0:
            result.append(c)

        # a -> b
        water = min(a, B - b)  # A에 가진것과, B의 여유분 중 더 작은만큼이 이동가능한 양
        pour(a - water, b + water)
        # a -> c
        water = min(a, C - c)
        pour(a - water, b)
        # b -> a
        water = min(b, A - a)
        pour(a + water, b - water)
        # b -> c
        water = min(b, C - c)
        pour(a, b - water)
        # c -> a
        water = min(c, A - a)
        pour(a + water, b)
        # c -> b
        water = min(c, B - b)
        pour(a, b + water)


bfs()

print(*sorted(result))

"""
- BFS 풀이

- 출처: https://cijbest.tistory.com/14
"""
