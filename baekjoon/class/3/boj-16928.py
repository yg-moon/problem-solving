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

    for i in range(1, 7):
        if (pos + i) not in visited:
            if (pos + i) in ladder:
                q.append([ladder[pos + i], move + 1])
                visited.add(pos + i)
            elif (pos + i) in snake:
                q.append([snake[pos + i], move + 1])
                visited.add(pos + i)

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
- 시작: 7:00
- 첫 풀이: 7:15
- 디버깅: 8:00

주의: 뱀도 반드시 고려해야 된다.
- 최단 거리이동 이라서 거꾸로 내려 가는 뱀은 무시해도 되나 착각할 수 있지만
  7 - 50 사다리, 55 - 45 뱀, 47 - 94 사다리 이런 식으로 연결 될 경우도 있기에
  반드시 뱀도 포함하여 최단 거리를 계산해야 된다.

요약
- 사다리는 다 고려
- 뱀도 다 고려
- 사다리와 뱀이 없는 칸 중에 가능한 최대치 한칸

핵심
- 주사위로 직접 도달한 지점만 방문처리. (사다리나 뱀으로 도달한 지점은 처리하지 않음)
- 이유: 특정한 칸을 도착지점으로 하는 사다리나 뱀은 여러 개 일 수 있기 때문.
  즉, 사다리나 뱀의 도착지점은 여러 번 방문할 수 있어야 함.
"""
