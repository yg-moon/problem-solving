import collections
import sys

n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = collections.defaultdict(lambda: -1)
for c in coins:
    dp[c] = 1

for i in range(1, m + 1):
    min_cnt = sys.maxsize
    for c in coins:
        if i - c >= 1 and dp[i - c] != -1:
            min_cnt = min(min_cnt, dp[i - c])
    if min_cnt != sys.maxsize:
        dp[i] = min_cnt + 1

print(dp[m])
