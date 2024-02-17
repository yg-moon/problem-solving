def rotate(board):
    return list(map(list, zip(*board[::-1])))


# 하나의 빈 슬롯 or 퍼즐 조각을 찾는 함수
def dfs(condition, board, abs_pos, rel_pos, visited):
    i, j, x, y, target = condition
    visited[i][j] = 1
    abs_pos.append((i, j))
    rel_pos.append((x, y))
    dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dx, dy in dir:
        nx, ny = i + dx, j + dy
        if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board):
            continue
        elif board[nx][ny] == target and visited[nx][ny] == 0:
            abs_pos, rel_pos, visited = dfs(
                [nx, ny, x + dx, y + dy, target], board, abs_pos, rel_pos, visited
            )
    # abs_pos: 보드에 위치한 실제 좌표 목록
    # rel_pos: (0,0) 기준의 상대적인 좌표 목록
    # visited: 방문 여부를 업데이트한 기록
    return abs_pos, rel_pos, visited


# 보드의 빈 슬롯을 리턴
def get_slots(board):
    visited = [[0] * len(board) for _ in range(len(board))]
    slots = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0 and visited[i][j] == 0:
                _, rel_pos, new_visited = dfs([i, j, 0, 0, 0], board, [], [], visited)
                slots.append(rel_pos)
                visited = new_visited
    return slots  # [[슬롯1 좌표],[슬롯2 좌표],...]


# 퍼즐 조각을 리턴
def get_pieces(board):
    visited = [[0] * len(board) for _ in range(len(board))]
    abs_to_rel = {}
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1 and visited[i][j] == 0:
                abs_pos, rel_pos, new_visited = dfs(
                    [i, j, 0, 0, 1], board, [], [], visited
                )
                abs_to_rel[tuple(abs_pos)] = rel_pos
                visited = new_visited
    return abs_to_rel  # {(절대 좌표) : [상대 좌표]}


def solution(game_board, table):
    answer = 0
    empty_slots = get_slots(game_board)

    for _ in range(4):
        table = rotate(table)
        pieces = get_pieces(table)
        for abs_pos, rel_pos in pieces.items():
            if rel_pos in empty_slots:
                empty_slots.remove(rel_pos)
                for i, j in abs_pos:
                    table[i][j] = 0
                answer += len(rel_pos)

    return answer


"""
- 요약
    1. 게임보드의 빈 슬롯 모양을 전부 구한다.
        - [[슬롯1 상대 좌표들], [슬롯2 상대 좌표들], …] 형태로 저장한다.
    2. 테이블의 퍼즐 조각 모양을 전부 구한다.
        - {(절대 좌표) : [상대 좌표]} 형태로 저장한다.
    3. 일치하는 모양이 있다면 (상대 좌표로 비교)
        - 해당 슬롯은 빈 슬롯 목록에서 제외
        - 해당 퍼즐 조각은 테이블에서 제외 (절대 좌표 이용)
        - 해당 모양의 크기만큼 정답을 증가
    4. 테이블을 4번 회전시켜가며 퍼즐 조각 모양을 다시 구하면서 모든 경우를 확인한다.

- 원본 출처: https://hkim-data.tistory.com/160
"""
