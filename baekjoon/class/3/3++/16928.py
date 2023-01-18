# 뱀과 사다리 게임
from collections import defaultdict, deque

ladder = defaultdict(int)
snake = defaultdict(int)
N, M = map(int, input().split())
for _ in range(N):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    snake[a] = b

# BFS
q = deque([(1, 0)])  # (현재 위치, 움직인 횟수)
visited = set()
min_move = int(1e9)

while q:
    pos, move = q.popleft()
    if pos == 100:
        min_move = min(min_move, move)
    # 사다리 또는 뱀으로 이동하는 경우
    for i in range(1, 7):
        if (pos + i) not in visited:
            if (pos + i) in ladder:
                q.append([ladder[pos + i], move + 1])
                visited.add(pos + i)
            elif (pos + i) in snake:
                q.append([snake[pos + i], move + 1])
                visited.add(pos + i)
    # 주사위를 굴려서 이동하는 경우
    for i in range(6, 0, -1):
        if (
            (pos + i) not in visited
            and (pos + i) not in ladder
            and (pos + i) not in snake
            and (pos + i) <= 100
        ):
            q.append([pos + i, move + 1])
            visited.add(pos + i)
            break

print(min_move)

"""
- 난이도: 골드5
- 분류: BFS

요약
- 3가지 경우를 고려한다.
    - 사다리로 가는 경우
    - 뱀으로 가는 경우
    - 사다리와 뱀이 없는 칸중 가능한 최대로 가는 경우

디버깅
- 주의: 뱀도 반드시 고려해야 한다.
    - 이유: 최단거리라서 거꾸로 내려가는 뱀은 무시해도 되나 착각할 수 있지만
        7 - 50 사다리, 55 - 45 뱀, 47 - 94 사다리 처럼 연결될 경우도 있기에
        반드시 뱀도 포함하여 계산해야 된다.

핵심
- 사다리나 뱀으로 도착한 지점은 방문처리 하지 않는다.
    - <=> 사다리의 시작점, 뱀의 시작점, 주사위로 도착한 지점만 방문처리한다.
    - 이유: 특정한 칸을 도착점으로 하는 사다리나 뱀은 여러개일 수 있기 때문.
        따라서 사다리와 뱀의 도착점은 여러번 방문할 수 있어야 한다.
"""
