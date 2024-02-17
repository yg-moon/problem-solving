# 숨바꼭질 3
from collections import deque

N, K = map(int, input().split())
q = deque([(N, 0)])  # (위치, 시간)
visited = set()

while q:
    pos, time = q.popleft()
    if pos == K:
        print(time)
        break
    else:
        # 순간이동
        next_pos = 2 * pos
        if 0 <= next_pos <= 100000 and next_pos not in visited:
            q.append((next_pos, time))
            visited.add(next_pos)
        # 걷기
        for next_pos in [pos - 1, pos + 1]:
            if 0 <= next_pos <= 100000 and next_pos not in visited:
                q.append((next_pos, time + 1))
                visited.add(next_pos)

"""
- 난이도: 골드5
- 분류: BFS

- 시리즈: 1697번 숨바꼭질
    - 차이점: 순간이동을 하는 경우 1초 후가 아닌 0초 후에 이동.
    - 해결: 순간이동을 먼저 모두 처리한 이후에 걷기를 처리.
"""
