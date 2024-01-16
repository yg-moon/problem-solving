from collections import deque

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            Rx, Ry = i, j
        if board[i][j] == "B":
            Bx, By = i, j


# 움직인 이후의 위치와 거리를 리턴
def move(x, y, dx, dy):
    dist = 0
    while board[x + dx][y + dy] != "#" and board[x][y] != "O":
        x += dx
        y += dy
        dist += 1
    return x, y, dist


def bfs():
    q = deque()
    q.append((Rx, Ry, Bx, By, 0))
    visited = set()
    visited.add((Rx, Ry, Bx, By))

    while q:
        rx, ry, bx, by, move_cnt = q.popleft()

        if board[rx][ry] == "O":
            return move_cnt

        for i in range(4):
            nrx, nry, r_dist = move(rx, ry, dx[i], dy[i])
            nbx, nby, b_dist = move(bx, by, dx[i], dy[i])

            # 파란 구슬이 구멍에 들어간 경우, 실패
            if board[nbx][nby] == "O":
                continue

            # 두 공의 위치가 같을 경우, 하나를 조정
            if nrx == nbx and nry == nby:
                # 이동거리가 많은 것이 이동 전에 뒤에 위치해있던 구슬이므로, 한칸 반대로 이동
                if r_dist > b_dist:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if move_cnt < 10 and (nrx, nry, nbx, nby) not in visited:
                q.append((nrx, nry, nbx, nby, move_cnt + 1))
                visited.add((nrx, nry, nbx, nby))

    return -1


print(bfs())

"""
- 더 간결한 풀이
    1. 보드의 내용을 직접 수정하지 않고, 좌표만 사용
        - 따라서 매번 그래프 상태를 복사할 필요가 없음
    2. 위치가 겹칠 경우, 이동한 거리를 기준으로 판단하여 조정
        - 이 아이디어 덕분에 직접 수정할 필요가 없음

- 출처: https://tooo1.tistory.com/506
"""
