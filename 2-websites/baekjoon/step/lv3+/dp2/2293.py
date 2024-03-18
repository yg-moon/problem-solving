# 동전 1
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# dp[i]: i원을 만들 수 있는 경우의 수
dp = [0] * (K + 1)

# 초기화
dp[0] = 1

# 각 동전에 대해 돌며, 동전 이상의 금액에 대해 갱신
for coin in coins:
    for i in range(coin, K + 1):
        dp[i] += dp[i - coin]

print(dp[K])

"""
- 난이도: 골드5
- 분류: dp
- 유형: 1차원 배열값을 갱신하는 dp
"""
