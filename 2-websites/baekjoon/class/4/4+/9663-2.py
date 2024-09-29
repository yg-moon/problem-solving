# N-Queen
def is_safe(row):
    # 이전 행까지만 확인
    for i in range(row):
        # 같은 열에 다른 퀸이 있는 경우 or 대각선에 다른 퀸이 있는 경우
        if board[row] == board[i] or abs(board[row] - board[i]) == abs(row - i):
            return False
    return True


def solve(row):
    global answer
    if row == N:
        answer += 1
        return
    for col in range(N):
        board[row] = col  # (row,col)에 퀸 놓기
        if is_safe(row):
            solve(row + 1)  # 다음 행에서 재귀


N = int(input())
board = [0] * N
answer = 0

solve(0)

print(answer)

"""
- 난이도: 골드4
- 분류: 브루트포스, 백트래킹

요약
- 첫 row부터 한줄씩 채워나가며 확인하는 방식
- 즉, 퀸을 첫 행부터 내려가면서 두며 재귀적으로 모든 경우를 확인

핵심
- 퀸의 위치는 1차원 배열만으로도 표현할 수 있다.
    - 하나의 행에는 하나의 퀸만 들어간다는 사실을 이용.
- 대각선 조건: x축과 y축의 차이가 같을 때.
    - 찾는 방법: 고려할 경우를 나누고, 예시 좌표를 놓고 패턴을 찾기.

참고: https://seongonion.tistory.com/103
"""
