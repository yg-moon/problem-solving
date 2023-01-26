# 구간 합 구하기 5
# 출처: https://castlerain.tistory.com/100
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
csum = [[0] * (N + 1) for _ in range(N + 1)]

# 누적합 배열 만들기
for i in range(1, N + 1):
    for j in range(1, N + 1):
        # csum[i][j]: (0,0) ~ (i,j) 사각형의 누적합
        csum[i][j] = (
            # (가로 구간) + (세로 구간) - (겹쳐서 더한 구간) + (원래 데이터의 값)
            csum[i - 1][j]
            + csum[i][j - 1]
            - csum[i - 1][j - 1]
            + arr[i - 1][j - 1]  # 주의: 입력은 (1,1) 기준으로 주어지므로 좌표를 보정
        )

# 구간 합 구하기
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    # (전체 구간) - (가로 구간) - (세로 구간) + (겹쳐서 뺀 구간)
    print(csum[x2][y2] - csum[x1 - 1][y2] - csum[x2][y1 - 1] + csum[x1 - 1][y1 - 1])

"""
- 난이도: 실버1
- 분류: 누적합 (2차원)
"""
