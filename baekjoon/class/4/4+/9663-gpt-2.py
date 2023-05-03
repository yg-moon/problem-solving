# Optimized version
def solve(col):
    global cnt
    if col == N:
        cnt += 1
        return
    for row in range(N):
        # is_safe를 대신함
        if columns[row] or diag1[row - col + N - 1] or diag2[row + col]:
            continue
        columns[row] = diag1[row - col + N - 1] = diag2[row + col] = True
        board[row][col] = 1
        solve(col + 1)
        columns[row] = diag1[row - col + N - 1] = diag2[row + col] = False
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
- 현재 상태(열, 대각, 역대각)를 저장하여 중복 확인을 줄여서 효율성 개선

배운점
- diag1[row - col + N - 1]로 하나의 주대각선(왼쪽 위~ 오른쪽 아래)에 대해 유일한 좌표를 얻을 수 있다.
    - 주대각선은 모든 i와 j의 차이가 같기 때문
    - N - 1을 더하는 이유는 음수가 되지 않게 하기 위해서
- diag2[row + col]로 하나의 역대각선에 대해 유일한 좌표를 얻을 수 있다.
    - 역대각선은 모든 i와 j의 합이 같기 때문
- 대각선의 총 개수는 2N-1개 (첫 행과 첫 열에서 시작하는 대각선의 개수를 세보면 됨)

예시
00 01 02 03
10 11 12 13
20 21 22 23
30 31 32 33
"""
