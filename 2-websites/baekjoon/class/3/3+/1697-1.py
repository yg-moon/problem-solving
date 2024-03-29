# 숨바꼭질
from collections import deque

N, K = map(int, input().split())

q = deque([(N, 0)])
visited = set()

while q:
    pos, time = q.popleft()
    if pos == K:
        print(time)
        break
    else:
        for next_pos in [pos - 1, pos + 1, 2 * pos]:
            if 0 <= next_pos <= 100000 and next_pos not in visited:
                q.append((next_pos, time + 1))
                visited.add(next_pos)

"""
- 난이도: 실버1
- 분류: BFS

디버깅
- 메모리 초과
    - visited를 (위치, 시간)으로 검사했던 것이 문제였음. -> 위치만 검사하도록 바꾸니 해결.
    - 이유: BFS이므로 큐에 먼저 들어온 위치는 항상 최소 시간임이 보장되기 때문.
"""
