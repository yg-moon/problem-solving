# 구슬 탈출 2
from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빨간 구슬, 파란 구슬, 구멍 위치 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            Rx, Ry = i, j
        elif board[i][j] == "B":
            Bx, By = i, j
        elif board[i][j] == "O":
            Hx, Hy = i, j


# 각 방향으로 기울이기
def slide(rx, ry, bx, by, board, dir):
    # 구슬 골인 여부
    red_in = False
    blue_in = False

    # 핵심: 어느 공을 먼저 움직일지? -> 빨파빨파
    # 빨간 구슬 이동1
    crx, cry = rx, ry
    while True:
        nrx = crx + dx[dir]
        nry = cry + dy[dir]
        # 범위를 벗어날 경우, 다음 칸이 벽이거나, 반대 구슬일 경우: 멈추기
        if (
            not (0 <= nrx < N and 0 <= nry < M)
            or board[nrx][nry] == "#"
            or board[nrx][nry] == "B"
        ):
            break
        # 다음 칸이 구멍인 경우: 골인
        elif board[nrx][nry] == "O":
            board[crx][cry] = "."
            red_in = True
            crx = nrx
            cry = nry
            break
        # 다음 칸이 빈칸인 경우: 이동
        elif board[nrx][nry] == ".":
            board[nrx][nry], board[crx][cry] = board[crx][cry], board[nrx][nry]
            crx = nrx
            cry = nry

    # 파란 구슬 이동1
    cbx, cby = bx, by
    while True:
        nbx = cbx + dx[dir]
        nby = cby + dy[dir]
        if (
            not (0 <= nbx < N and 0 <= nby < M)
            or board[nbx][nby] == "#"
            or board[nbx][nby] == "R"
        ):
            break
        elif board[nbx][nby] == "O":
            board[cbx][cby] = "."
            blue_in = True
            cbx = nbx
            cby = nby
            break
        elif board[nbx][nby] == ".":
            board[nbx][nby], board[cbx][cby] = board[cbx][cby], board[nbx][nby]
            cbx = nbx
            cby = nby

    # 빨간 구슬 이동2
    if not (red_in or blue_in):
        while True:
            nrx = crx + dx[dir]
            nry = cry + dy[dir]
            if (
                not (0 <= nrx < N and 0 <= nry < M)
                or board[nrx][nry] == "#"
                or board[nrx][nry] == "B"
            ):
                break
            elif board[nrx][nry] == "O":
                board[crx][cry] = "."
                red_in = True
                crx = nrx
                cry = nry
                break
            elif board[nrx][nry] == ".":
                board[nrx][nry], board[crx][cry] = board[crx][cry], board[nrx][nry]
                crx = nrx
                cry = nry

    # 파란 구슬 이동2
    if not blue_in:
        while True:
            nbx = cbx + dx[dir]
            nby = cby + dy[dir]
            if (
                not (0 <= nbx < N and 0 <= nby < M)
                or board[nbx][nby] == "#"
                or board[nbx][nby] == "R"
            ):
                break
            elif board[nbx][nby] == "O":
                board[cbx][cby] = "."
                blue_in = True
                cbx = nbx
                cby = nby
                break
            elif board[nbx][nby] == ".":
                board[nbx][nby], board[cbx][cby] = board[cbx][cby], board[nbx][nby]
                cbx = nbx
                cby = nby

    # 실패: 파란 구슬이 구멍에 빠지거나, 아무 구슬도 움직이지 않았을 경우
    if blue_in or ((rx, ry, bx, by) == (crx, cry, cbx, cby)):
        is_fail = True
    else:
        is_fail = False

    return crx, cry, cbx, cby, board, is_fail


# BFS로 최소 횟수 찾기
def bfs():
    q = deque()
    q.append((Rx, Ry, Bx, By, board, 0))
    # 방문여부 확인: 빨간 구슬과 파란 구슬의 위치
    visited = set()
    visited.add((Rx, Ry, Bx, By))

    while q:
        rx, ry, bx, by, cur_board, move_cnt = q.popleft()

        if rx == Hx and ry == Hy:
            return move_cnt

        for dir in range(4):
            # 주의: 보드의 상태를 deecopy 해야함!
            nrx, nry, nbx, nby, nxt_board, is_fail = slide(
                rx, ry, bx, by, deepcopy(cur_board), dir
            )
            if not is_fail and move_cnt < 10 and (nrx, nry, nbx, nby) not in visited:
                q.append((nrx, nry, nbx, nby, nxt_board, move_cnt + 1))
                visited.add((nrx, nry, nbx, nby))

    return -1


print(bfs())

"""
- 난이도: 골드1
- 분류: 시뮬레이션, BFS
- 소요 시간: 2시간 (구상 5분, 구현 1시간 30분, 디버깅 30분)

요약
- BFS를 이용해서 최소 몇번 움직여야 하는지 찾기
    - 현재 상태에서 4방향으로 기울이기를 시도
    - 구슬이 안 움직이거나 실패할 경우 큐에 넣지 않기

핵심
- 방문여부: 두 구슬의 좌표를 기준으로
- 기울이기: 빨파빨파 순으로 움직이기

디버깅
- 상황: 코드가 의도대로 동작하지 않음
- 원인: board를 deepcopy 안했더니 꼬였음
"""
