# 사탕 게임
N = int(input())
board = [list(input()) for _ in range(N)]
dx = [-1, 0]
dy = [0, 1]
answer = 0


def check():
    global answer
    # 가로
    for i in range(N):
        cnt = 1  # 주의: 행마다 초기화 해야함
        for j in range(1, N):
            if board[i][j] == board[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt)
    # 세로
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[i][j] == board[i - 1][j]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt)


for x in range(N):
    for y in range(N):
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[x][y] != board[nx][ny]:
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]  # swap
                check()
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]  # 원상복구

print(answer)

"""
- 난이도: 실버2
- 분류: 완전탐색

- 요약: 모든 좌표를 보면서, 둘이 다르면 교체해보고, 최장연속부분을 찾기
- 주의
    - 바꾼 사탕들과 전혀 상관없는 곳에서 정답이 나올 수 있으므로 전부 검사해야 함 (ex. 예제2)
    - 가장 긴 줄이 여러개라도 그 중 하나만 정답으로 취급함
- 개선점
    - 불필요한 중복탐색 제거: 상하좌우로 전부 볼 필요없이, 오른쪽과 아래쪽으로만 확인해도 됨
    - 간결한 로직: 연속부분 찾을때 cur을 저장할 필요없이, 인접한 원소끼리만 비교해도 됨
    - 참고: https://yuna0125.tistory.com/131
"""
