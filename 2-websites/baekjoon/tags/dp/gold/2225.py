# 합분해
N, K = map(int, input().split())

MOD = int(1e9)

# dp[i][j]: i개를 더해서 합이 j가 되는 경우의 수
dp = [[0] * (N + 1) for _ in range(K + 1)]

# 초기화
for j in range(N + 1):
    dp[1][j] = 1

# 점화식
for i in range(2, K + 1):
    for j in range(N + 1):
        for k in range(N + 1):
            if j - k >= 0:
                dp[i][j] += (dp[i - 1][j - k]) % MOD

print(dp[K][N] % MOD)

"""
- 난이도: 골드5
- 분류: dp
- 소요 시간: 30분

- 요약: 직전의 결과를 이용하여 가능한 모든 경우를 갱신하는 2차원 dp 유형
"""
