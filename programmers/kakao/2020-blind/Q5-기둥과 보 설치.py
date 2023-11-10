def is_ok(board, result):
    def pillar_cond_2(x, y):
        return board[1][x][y] or board[1][x - 1][y]

    def pillar_cond_3(x, y):
        return board[0][x][y - 1]

    def beam_cond_1(x, y):
        return board[0][x][y - 1] or board[0][x + 1][y - 1]

    def beam_cond_2(x, y):
        return board[1][x - 1][y] and board[1][x + 1][y]

    # 모든 구조물이 설치조건을 만족하는지 확인
    for x, y, a in result:
        # 기둥
        if a == 0:
            # 1.바닥 위에 있거나, 2.보의 한쪽 끝 부분 위에 있거나, 3.다른 기둥 위에 있어야 함
            if not (y == 0 or pillar_cond_2(x, y) or pillar_cond_3(x, y)):
                return False
        # 보
        elif a == 1:
            # 1.한쪽 끝 부분이 기둥 위에 있거나, 2.양쪽 끝 부분이 다른 보와 연결 되어야 함
            if not (beam_cond_1(x, y) or beam_cond_2(x, y)):
                return False
    return True


def solution(n, build_frame):
    # board[0][x][y] == True: (x,y)에 기둥이 설치되어 있음
    # board[1][x][y] == True: (x,y)에 보가 설치되어 있음
    board = [[[False] * (n + 1) for _ in range(n + 1)] for _ in range(2)]
    result = []

    # 시뮬레이션 & 전수조사
    for x, y, a, b in build_frame:
        # 삭제: 삭제해보고, 조건을 만족하면 진행, 아니면 되돌리기
        if b == 0:
            board[a][x][y] = False
            result.remove([x, y, a])
            if not is_ok(board, result):
                board[a][x][y] = True
                result.append([x, y, a])
        # 설치: 설치해보고, 조건을 만족하면 진행, 아니면 되돌리기
        elif b == 1:
            board[a][x][y] = True
            result.append([x, y, a])
            if not is_ok(board, result):
                board[a][x][y] = False
                result.remove([x, y, a])

    return sorted(result)


"""
- 분류: 구현, 시뮬레이션, 완전탐색
- 시간: 2:00-3:00 (60분)
"""
