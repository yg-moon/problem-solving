N, M = map(int, input().split())
A, B, dir = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

LAND = 0
SEA = 1
VISITED = 2

# NESW
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph[A][B] = VISITED
cnt = 1

# 왼쪽으로 회전
def turn_left(d):
    if d == 0:
        return 3
    return d - 1


while True:
    moved = False
    for _ in range(4):
        dir = turn_left(dir)
        na = A + dx[dir]
        nb = B + dy[dir]
        if graph[na][nb] == LAND:
            graph[na][nb] = VISITED
            A = na
            B = nb
            cnt += 1
            moved = True
            break

    # 움직이지 않은 경우, 뒤로 가보기
    if not moved:
        na = A - dx[dir]
        nb = B - dy[dir]
        # 뒤로 방문할 수 없는 경우, 게임종료
        if graph[na][nb] != LAND:
            break
        # 뒤로 가기
        A = na
        B = nb

print(cnt)
