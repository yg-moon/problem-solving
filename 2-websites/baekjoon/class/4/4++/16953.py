# A -> B
from collections import deque

A, B = map(int, input().split())
answer = -1


def bfs():
    global answer
    q = deque([(A, 1)])
    visited = set()
    while q:
        num, cnt = q.popleft()
        if num == B:
            answer = cnt
            return
        for nxt_num in [2 * num, int(str(num) + "1")]:
            if nxt_num not in visited and nxt_num <= int(1e9):
                q.append((nxt_num, cnt + 1))
                visited.add(nxt_num)


bfs()

print(answer)

"""
- 난이도: 실버2
- 분류: BFS

디버깅
- "BFS 도중 범위를 넘어가는 경우가 있다고 해서, 큐에 남은 것들도 목표에 도달하지 못하는 것은 아니다."
"""
