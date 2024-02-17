from collections import deque


# 핵심1: 현재 상태에서 로봇이 회전해서 갈 수 있는 좌표들을 구하기
def get_rotations(new_board, pos1, pos2):
    results = []

    def append_results(x1, y1, x2, y2):
        # 두 칸이 모두 비어있는 경우에만 회전 가능
        if new_board[x1][y1] == 0 and new_board[x2][y2] == 0:
            results.append((pos1, (x1, y1)))
            results.append((pos2, (x2, y2)))

    # 가로로 놓인 경우
    if pos1[0] == pos2[0]:
        # 위를 확인
        x1, y1 = pos1[0] - 1, pos1[1]
        x2, y2 = pos2[0] - 1, pos2[1]
        append_results(x1, y1, x2, y2)
        # 아래를 확인
        x1, y1 = pos1[0] + 1, pos1[1]
        x2, y2 = pos2[0] + 1, pos2[1]
        append_results(x1, y1, x2, y2)

    # 세로로 놓인 경우
    elif pos1[1] == pos2[1]:
        # 왼쪽을 확인
        x1, y1 = pos1[0], pos1[1] - 1
        x2, y2 = pos2[0], pos2[1] - 1
        append_results(x1, y1, x2, y2)
        # 오른쪽을 확인
        x1, y1 = pos1[0], pos1[1] + 1
        x2, y2 = pos2[0], pos2[1] + 1
        append_results(x1, y1, x2, y2)

    return results


def solution(board):
    N = len(board)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    start = ((1, 1), (1, 2))
    min_time = int(1e9)

    # -1로 패딩 (조건검사 간소화)
    new_board = [[-1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]

    # BFS
    # 핵심2: 좌표 2개를 set으로 묶어서 방문여부 확인
    q = deque()
    q.append((0, start))
    visited = []
    visited.append(set(start))

    while q:
        time, (pos1, pos2) = q.popleft()
        if pos1 == (N, N) or pos2 == (N, N):
            min_time = min(min_time, time)
            continue
        # 4방향 이동
        for i in range(4):
            npos1 = (pos1[0] + dx[i], pos1[1] + dy[i])
            npos2 = (pos2[0] + dx[i], pos2[1] + dy[i])
            if (
                new_board[npos1[0]][npos1[1]] == 0
                and new_board[npos2[0]][npos2[1]] == 0
                and set((npos1, npos2)) not in visited
            ):
                q.append((time + 1, (npos1, npos2)))
                visited.append(set((npos1, npos2)))
        # 회전
        for npos1, npos2 in get_rotations(new_board, pos1, pos2):
            if set((npos1, npos2)) not in visited:
                q.append((time + 1, (npos1, npos2)))
                visited.append(set((npos1, npos2)))

    return min_time


"""
- 분류: 시뮬레이션, BFS
- 시간: 10:20-11:20 (60분)
"""
