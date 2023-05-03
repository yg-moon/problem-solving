# Optimized version
def solve(col):
    global cnt
    if col == N:
        cnt += 1
        return
    for row in range(N):
        # is_safe를 대신함
        if columns[row] or diag1[row + col] or diag2[row - col + N - 1]:
            continue
        columns[row] = diag1[row + col] = diag2[row - col + N - 1] = True
        board[row][col] = 1
        solve(col + 1)
        columns[row] = diag1[row + col] = diag2[row - col + N - 1] = False
        board[row][col] = 0


N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0

columns = [False] * N
diag1 = [False] * (2 * N - 1)
diag2 = [False] * (2 * N - 1)

solve(0)
print(cnt)

"""
- 첫 row부터 가로로 한줄씩 채워나가며 확인하는 방식
- 현재 상태(열, 대각, 역대각)를 저장하여 중복확인을 줄여서 효율성 개선

배운점
- diag1[row + col] 로 주대각선 (왼쪽위~오른쪽 아래)에 대해 유일한 좌표를 얻을 수 있다.
- diag2[row - col + N - 1] 로 역대각선에 대해 유일한 좌표를 얻을 수 있다.
- (well-known 이라고 함)
- 참고: 대각선의 총 개수는 2N-1개 (첫 행과 첫 열에서 시작하는 대각선의 개수를 세보면 됨)
"""
