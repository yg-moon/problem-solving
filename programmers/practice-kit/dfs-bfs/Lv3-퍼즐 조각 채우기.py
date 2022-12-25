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


def get_shapes(board, target):
    """
    - 이 함수는 두가지 경우에 대해 다른 동작을 한다.

    Case1. 게임보드의 빈 슬롯을 list로 리턴. (상대적인 좌표로)
        입력값:
            board = game_board
            target = 0
        리턴값:
            shapes = [[슬롯1 좌표],[슬롯2 좌표],...]

    Case2. 테이블의 퍼즐 조각들을 dict로 리턴.
        입력값:
            board = table
            target = 1
        리턴값:
            shapes = {(절대 좌표) : [상대 좌표]}

    - 사실 함수를 분리해야 한다고 생각한다.
    - 상황에 따라 리턴타입이 달라지는 방식은 직관성이 떨어진다.
    """
    visited = [[0] * len(board) for _ in range(len(board))]
    shapes = {} if target == 1 else []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == target and visited[i][j] == 0:
                abs_pos, rel_pos, new_visited = dfs(
                    [i, j, 0, 0, target], board, [], [], visited
                )
                if target == 1:
                    shapes[tuple(abs_pos)] = rel_pos
                else:
                    shapes.append(rel_pos)
                visited = new_visited
    return shapes


def solution(game_board, table):
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
    """
    answer = 0
    empty_slots = get_shapes(game_board, 0)
    for _ in range(4):
        table = rotate(table)
        puzzle_pieces = get_shapes(table, 1)
        for abs_pos, rel_pos in puzzle_pieces.items():
            if rel_pos in empty_slots:
                empty_slots.remove(rel_pos)
                for i, j in abs_pos:
                    table[i][j] = 0
                answer += len(rel_pos)
    return answer


"""
- 원본 코드 출처: https://hkim-data.tistory.com/160
"""
