# 행렬 곱셈 순서
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i번째 행렬부터 j번째 행렬까지 곱하는 최소비용
dp = [[0] * N for _ in range(N)]

for gap in range(1, N):
    for i in range(N - gap):
        j = i + gap
        dp[i][j] = int(1e9)  # 주의: 여기서 초기화 해야함
        # 핵심: dp[i][j] = min[(i<=k<j){dp[i][k] + dp[k+1][j] + 행렬곱 비용}]
        for k in range(i, j):
            dp[i][j] = min(
                dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i][0] * arr[k][1] * arr[j][1]
            )

print(dp[0][N - 1])

"""
- 난이도: 골드3
- 분류: dp
- 유형: 구간 쪼개기 dp + 행렬곱

- 참고: https://claude-u.tistory.com/271
"""
