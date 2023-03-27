# 체스판 다시 칠하기 2
# 출처: https://jih3508.tistory.com/59
def min_change(color):
    # color: 좌상단 칸의 색깔 (B or W)

    # 2차원 누적합 배열 구하기
    # - 좌상단 색에 따른 정답패턴과, 현재 실제 보드의 패턴을 비교
    # - 정답패턴과 같으면 0, 다르면 1로 두고 누적합 계산
    psum = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            # 팁: 정답패턴에서 (행+열)좌표의 값이 짝수면 좌상단 칸의 색과 같음
            if (i + j) % 2 == 0:
                # 바꿔야 하는 부분만 1로 표시
                val = 0 if board[i][j] == color else 1
            else:
                val = 1 if board[i][j] == color else 0
            # (좌상, 상, 좌) 3방향만 확인하므로 진행하면서 바로 계산해도 무관
            psum[i + 1][j + 1] = psum[i][j + 1] + psum[i + 1][j] - psum[i][j] + val

    # K*K 크기의 구간합중 최솟값 구하기
    min_cnt = int(1e9)
    for i in range(1, N - K + 2):
        for j in range(1, M - K + 2):
            min_cnt = min(
                min_cnt,
                psum[i + K - 1][j + K - 1]
                - psum[i + K - 1][j - 1]
                - psum[i - 1][j + K - 1]
                + psum[i - 1][j - 1],
            )
    return min_cnt


N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]
print(min(min_change("B"), min_change("W")))

"""
- 난이도: 골드5
- 분류: 누적합

막힌 곳
- 누적합인데 번갈아서 칠하는걸 어떻게 확인하지?

요약
- 1. 정답패턴과 비교하여, 바꿔야 하는 칸을 1로 두고 누적합 계산
- 2. 좌상단 색에 따라 2가지 경우로 구분하고, (행+열)좌표의 홀짝으로 간단하게 판정
- 3. K*K 크기의 구간합중 최솟값 구하기
- 누적합 배열 다룰 때 인덱스 정확하게 신경쓰기
"""
