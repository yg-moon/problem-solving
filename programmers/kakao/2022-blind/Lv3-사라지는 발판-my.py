# 실패. (최적의 전략을 수행한 결과가 아니라 그냥 완전탐색이라서)
total_moves = [int(1e9)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def solution(board, aloc, bloc):
    dfs(board, aloc, bloc, "A", 0, check_same(aloc, bloc))
    return min(total_moves)


def dfs(board, aloc, bloc, turn, moves, same_spot):
    if same_spot:
        total_moves.append(moves)
        return

    if check_same(aloc, bloc):
        same_spot = True

    # 누구 차례인지 확인 & 다음 갈 곳을 확인
    if turn == "A":
        next_pos = find_next(board, aloc)
    else:
        next_pos = find_next(board, bloc)

    if not next_pos:
        total_moves.append(moves)
        return

    # 다음 위치에 대해 재귀
    for pos in next_pos:
        if turn == "A":
            board[aloc[0]][aloc[1]] = 0
            dfs(board[:], pos, bloc, next_turn(turn), moves + 1, same_spot)
            board[aloc[0]][aloc[1]] = 1
        else:
            board[bloc[0]][bloc[1]] = 0
            dfs(board[:], aloc, pos, next_turn(turn), moves + 1, same_spot)
            board[bloc[0]][bloc[1]] = 1


# 같은 위치에 있는지 확인
def check_same(aloc, bloc):
    if aloc == bloc:
        return True
    return False


# 다음 차례 리턴
def next_turn(player):
    if player == "A":
        return "B"
    else:
        return "A"


# 상하좌우 중 갈 수 있는 칸들을 리턴
def find_next(board, loc):
    next_pos = []
    R, C = len(board), len(board[0])
    for i in range(4):
        nx = loc[0] + dx[i]
        ny = loc[1] + dy[i]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == 1:
            next_pos.append([nx, ny])
    return next_pos


# 핵심: 서로 최선의 플레이를 펼쳐야 한다.
# - 끝났을 때 움직인 횟수를 기록. 최솟값이 정답.

# dfs (보드 상태, A위치, B위치, 누구 차례, 총 움직인 횟수)
# 움직일수 있는 칸중에 하나를 선택해서 이동
