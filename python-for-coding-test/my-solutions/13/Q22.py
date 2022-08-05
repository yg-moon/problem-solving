# Kakao 2020
# 출처: 이코테
from collections import deque


def get_next_pos(pos, board):
    next_pos = []  # 리턴값: 현재 위치에서 이동할 수 있는 위치들
    pos = list(pos)  # 변환: set -> list
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # 이동: 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = (
            pos1_x + dx[i],
            pos1_y + dy[i],
            pos2_x + dx[i],
            pos2_y + dy[i],
        )
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if (
            board[pos1_next_x][pos1_next_y] == 0
            and board[pos2_next_x][pos2_next_y] == 0
        ):
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})

    # 회전
    # 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        # 위쪽 또는 아래쪽으로 회전
        for i in [-1, 1]:
            # 위쪽과 아래쪽 두 칸이 모두 비어 있다면, 두 경우 다 추가
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        # 왼쪽 또는 오른쪽으로 회전
        for i in [-1, 1]:
            # 왼쪽과 오른쪽 두 칸이 모두 비어 있다면, 두 경우 다 추가
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    return next_pos


def solution(board):
    # 맵 외곽에 벽 두르기
    N = len(board)
    new_board = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]
    # BFS
    Q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    Q.append((pos, 0))
    visited.append(pos)
    while Q:
        pos, time = Q.popleft()
        if (N, N) in pos:
            return time
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                Q.append((next_pos, time + 1))
                visited.append(next_pos)
    return 0
