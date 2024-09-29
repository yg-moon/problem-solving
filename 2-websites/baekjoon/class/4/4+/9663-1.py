# 나이브 버전: 시간초과
def is_safe(r, c):
    # 현재 행의 좌측 확인
    for j in range(c):
        if board[r][j] == 1:
            return False

    # 좌측 상단 대각선 확인
    i = r
    j = c
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # 좌측 하단 대각선 확인
    i = r
    j = c
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve(col):
    global answer
    if col == N:
        answer += 1
        return
    for row in range(N):
        if is_safe(row, col):
            board[row][col] = 1
            solve(col + 1)
            board[row][col] = 0


N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
answer = 0

solve(0)
print(answer)

"""
- 세로로 한줄씩 채워나가며 확인하는 방식
- 퀸을 채우는 순서 때문에, 왼쪽 방향만 확인하면 됨
- 다만 모든 row, col을 직접 확인하기 때문에 비효율적
"""
