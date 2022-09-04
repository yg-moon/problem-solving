# Kakao 2020
# 시간 초과 (BFS가 아닌 DFS 완전탐색이기 때문)
def solution(board):
    N = len(board)
    answer = [int(1e9)]

    def move(r1, r2, dir):
        pos = []  # 이동 가능한 위치들
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
            pos.append((nx1, ny1))
            pos.append((nx2, ny2))
        return pos

    def rotate(r1, r2):
        pos = []
        # 가로
        if r1[0] == r2[0]:
            # 위쪽 or 아래쪽으로 회전 가능
            for i in [-1, 1]:
                nx1 = r1[0] + i
                nx2 = r2[0] + i
                if (
                    0 <= nx1 < N
                    and 0 <= nx2 < N
                    and board[nx1][r1[1]] == 0
                    and board[nx2][r2[1]] == 0
                ):
                    pos.append([r1, (nx1, r1[1])])
                    pos.append([(nx2, r2[1]), r2])
        # 세로
        elif r1[1] == r2[1]:
            # 왼쪽 or 오른쪽으로 회전 가능
            for i in [-1, 1]:
                ny1 = r1[1] + i
                ny2 = r2[1] + i
                if (
                    0 <= ny1 < N
                    and 0 <= ny2 < N
                    and board[r1[0]][ny1] == 0
                    and board[r2[0]][ny2] == 0
                ):
                    pos.append([(r1[0], ny1), r1])
                    pos.append([(r2[0], ny2), r2])
        return pos

    def dfs(time, r1, r2, visited):
        # 중복일 경우
        if {r1, r2} in visited:
            return

        # 목표에 도달한 경우
        if r1 == (N - 1, N - 1) or r2 == (N - 1, N - 1):
            answer.append(time)
            return

        # 방문 기록
        visited.append({r1, r2})

        # 이동 가능하면 이동
        dir = ["up", "down", "left", "right"]
        for d in dir:
            move_result = move(r1, r2, d)
            if move_result:
                time += 1
                dfs(time, move_result[0], move_result[1], visited[:])
                time -= 1

        # 회전 가능하면 회전
        rotate_result = rotate(r1, r2)
        if rotate_result:
            for r in rotate_result:
                time += 1
                dfs(time, r[0], r[1], visited[:])
                time -= 1

    dfs(0, (0, 0), (0, 1), [])
    return min(answer)
