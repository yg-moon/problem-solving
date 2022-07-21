# 실패. (BFS가 아닌 DFS로 풀었고, 회전분기 제대로 나누지 못했음.)
def solution(board):
    N = len(board)
    answer = [1e9]

    def move(r1, r2, dir):
        nx1, ny1 = r1[0], r1[1]
        nx2, ny2 = r2[0], r2[1]
        if dir == "up":
            nx1 -= 1
            nx2 -= 1
        elif dir == "down":
            nx1 += 1
            nx2 += 1
        elif dir == "left":
            ny1 -= 1
            ny2 -= 1
        elif dir == "right":
            ny1 += 1
            ny2 += 1
        if (
            0 <= nx1 < N
            and 0 <= ny1 < N
            and 0 <= nx2 < N
            and 0 <= ny2 < N
            and board[nx1][ny1] == 0
            and board[nx2][ny2] == 0
        ):
            return [True, (nx1, ny1), (nx2, ny2)]
        return [False]

    def rotate(r1, r2, dir):
        # 가로
        if r1[0] == r2[0]:
            if dir == "clock":
                nx1 = r1[0]
                ny1 = r1[1]
                nx2 = r2[0] + 1
                ny2 = r2[1] - 1
                nx3 = r2[0] + 1
                ny3 = r2[1]
            elif dir == "anticlock":
                nx1 = r2[0]
                ny1 = r2[1]
                nx2 = r1[0] + 1
                ny2 = r1[1] + 1
                nx3 = r1[0] + 1
                ny3 = r1[1]
        # 세로
        else:
            if dir == "clock":
                nx1 = r2[0]
                ny1 = r2[1]
                nx2 = r1[0] + 1
                ny2 = r1[1] + 1
                nx3 = r1[0]
                ny3 = r1[1] + 1
            elif dir == "anticlock":
                nx1 = r1[0] + 1
                ny1 = r1[1] - 1
                nx2 = r2[0]
                ny2 = r2[1]
                nx3 = r1[0]
                ny3 = r1[1] - 1
        if (
            0 <= nx1 < N
            and 0 <= ny1 < N
            and 0 <= nx2 < N
            and 0 <= ny2 < N
            and 0 <= nx3 < N
            and 0 <= ny3 < N
            and board[nx1][ny1] == 0
            and board[nx2][ny2] == 0
            and board[nx3][ny3] == 0
        ):
            return [True, (nx1, ny1), (nx2, ny2)]
        return [False]

    visited = set()

    def dfs(time, r1, r2):
        # 중복일 경우
        if (r1, r2) in visited:
            return

        # 목표에 도달한 경우
        if r1 == (N - 1, N - 1) or r2 == (N - 1, N - 1):
            answer.append(time)

        # 방문 기록
        visited.add((r1, r2))

        # 이동 가능하면 이동
        dir = ["up", "down", "left", "right"]
        for d in dir:
            move_result = move(r1, r2, d)
            if move_result[0]:
                time += 1
                dfs(time, move_result[1], move_result[2])
                time -= 1

        # 회전 가능하면 회전
        rotate_clock = rotate(r1, r2, "clock")
        if rotate_clock[0]:
            time += 1
            dfs(time, rotate_clock[1], rotate_clock[2])
            time -= 1
        rotate_anticlock = rotate(r1, r2, "anticlock")
        if rotate_anticlock[0]:
            time += 1
            dfs(time, rotate_anticlock[1], rotate_anticlock[2])
            time -= 1

    dfs(0, (0, 0), (0, 1))

    return min(answer)

board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
]
print(solution(board))
