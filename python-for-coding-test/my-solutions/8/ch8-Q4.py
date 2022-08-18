import collections

N = int(input())
dp = collections.defaultdict(int)

dp[1] = 1
dp[2] = 3
for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 796796

print(dp[N])
