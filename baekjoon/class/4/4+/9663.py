# N-Queen
# 출처: https://seongonion.tistory.com/103
def is_safe(row):
    # x의 이전 행까지만 확인
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
- 첫 row부터 가로로 한줄씩 채워나가며 확인하는 방식
- (즉 퀸을 맨 위의 행부터 순차적으로 내려가면서 두어, 재귀적으로 모든 경우를 확인한다.)

핵심
- 퀸의 위치를 표현하는 방법을 잘 고안하면 1차원 배열만으로도 해결할 수 있다.
    - 어차피 하나의 행에는 하나의 퀸만 들어간다는 사실을 이용.
- 대각선 조건: x축과 y축의 차이가 같을 때.
    - 찾는 방법: 고려할 경우를 나누고, 예시 좌표를 놓고 패턴을 찾기.

기타
- 의문: row 배열의 값이 이전 상태 그대로 쓰이는데 문제가 없으려나?
    - 해결: 어차피 퀸을 위에서부터 순차적으로 두고, x의 이전 행까지만 확인하기 때문에 상관없다.
"""
