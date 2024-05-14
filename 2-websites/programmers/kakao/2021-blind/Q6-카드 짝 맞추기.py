from itertools import permutations
from collections import deque, defaultdict

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = int(1e9)


# 해당 방향으로 ctrl을 눌러 움직였을때 도착하는 위치
def ctrl_pos(board, x, y, dir_x, dir_y):
    for step in range(1, 4):
        nx = x + dir_x * step
        ny = y + dir_y * step
        if 0 <= nx < 4 and 0 <= ny < 4:
            if board[nx][ny] > 0:
                return (nx, ny)
            last = step
    return (x + dir_x * last, y + dir_y * last)


# start에서 end까지 걸리는 최단거리 (BFS)
def calc_dist(board, start_pos, end_pos):
    q = deque([(start_pos, 0)])
    visited = set()
    visited.add(start_pos)
    while q:
        (x, y), dist = q.popleft()
        if (x, y) == end_pos:
            return dist
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) not in visited:
                q.append(((nx, ny), dist + 1))
                # ctrl을 누르는 경우도 고려하기
                q.append((ctrl_pos(board, x, y, dx[i], dy[i]), dist + 1))
    return -1


def solution(board, r, c):
    answer = INF
    card_pos = defaultdict(list)  # {카드 번호: [(좌표1), (좌표2), ...]}

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                card_pos[board[i][j]].append((i, j))

    # 각 순열마다 시뮬레이션
    for perm in permutations(list(card_pos.values())):
        move_cnt = 0
        cursor = [(r, c)]
        cur_board = [row[:] for row in board]
        # 각 번호에 대해
        for pos1, pos2 in perm:
            possible_moves = []  # [(거리1, 도착위치1), ...]
            for pos in cursor:
                # 방문하는 두가지 순서를 고려
                possible_moves.append(
                    (
                        calc_dist(cur_board, pos, pos1)
                        + calc_dist(cur_board, pos1, pos2),
                        pos2,
                    )
                )
                possible_moves.append(
                    (
                        calc_dist(cur_board, pos, pos2)
                        + calc_dist(cur_board, pos2, pos1),
                        pos1,
                    )
                )
            # 카드 제거
            cur_board[pos1[0]][pos1[1]] = 0
            cur_board[pos2[0]][pos2[1]] = 0
            # 다음 상태 업데이트
            possible_moves.sort()
            min_move = possible_moves[0][0]
            move_cnt += min_move + 2
            cursor = [next_pos for move, next_pos in possible_moves if move == min_move]
        answer = min(answer, move_cnt)

    return answer


"""
- 분류: 시뮬레이션, BFS

핵심
- 1. 몇번 카드부터 제거할지 순서를 결정하기 (permutation)
- 2. 해당 번호를 제거하는 다른 순서를 고려하기
- 3. 커서 이동은 BFS로 수행
"""
