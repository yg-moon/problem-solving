# Naive version
def is_safe(r, c):
    # Check the current row on the left side
    for j in range(c):
        if board[r][j] == 1:
            return False

    # Check upper diagonal on the left side
    i = r
    j = c
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i = r
    j = c
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve(col):
    global cnt
    if col == N:
        cnt += 1
        return
    for row in range(N):
        if is_safe(row, col):
            board[row][col] = 1
            solve(col + 1)
            board[row][col] = 0


N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0

solve(0)
print(cnt)

"""
- 첫 column 부터 세로로 한줄씩 채워나가며 확인하는 방식 (주의: row 부터 채워나가는게 아님)
- 다만 모든 row, col을 확인하기 때문에 비효율적이라서 백준에서는 시간초과.
"""
