import collections

x = int(input())
dp = collections.defaultdict(int)
# dp[0] = 0, dp[1] = 0 은 defaultdict가 처리해주므로 생략.

# Bottum-up
for i in range(2, x + 1):
    # -1 연산은 언제나 가능하므로, 기본값으로 써두기
    dp[i] = dp[i - 1] + 1
    # 나눌 수 있으면 나눠보고, 가장 낮은 총 연산 횟수를 최종적으로 기록
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[x])
