# 행렬 곱셈 순서
# 출처: https://claude-u.tistory.com/271
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: 구간 [i,j]을 곱하는 최소비용
dp = [[0] * N for _ in range(N)]

for gap in range(1, N):
    for i in range(N - gap):
        j = i + gap
        if gap == 1:
            dp[i][j] = arr[i][0] * arr[i][1] * arr[j][1]
        else:
            dp[i][j] = int(1e9)
            for k in range(i, j):
                # 핵심: 구간 쪼개기 + 행렬을 합치는 비용
                dp[i][j] = min(
                    dp[i][j],
                    dp[i][k] + dp[k + 1][j] + arr[i][0] * arr[k][1] * arr[j][1],
                )

print(dp[0][N - 1])

"""
- 난이도: 골드3
- 분류: dp

- 유형: 구간 쪼개기 dp + 행렬곱
"""
