INF = int(1e9)

N, M = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

dp = [INF] * (M + 1)
dp[0] = 0

# Bottom-up
for i in range(N):
    for j in range(coins[i], M + 1):
        # (i - k)원을 만드는 방법이 존재하는 경우
        if dp[j - coins[i]] != INF:
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

if dp[M] == INF:
    print(-1)
else:
    print(dp[M])
