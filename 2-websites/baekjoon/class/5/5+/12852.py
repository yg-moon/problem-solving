# 1로 만들기 2
N = int(input())

# dp[i]: i를 1로 만드는데 필요한 연산의 최소 횟수
dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

i = N
result = [N]

while i > 1:
    if i % 2 == 0 and dp[i // 2] == dp[i] - 1:
        i //= 2
    elif i % 3 == 0 and dp[i // 3] == dp[i] - 1:
        i //= 3
    elif dp[i - 1] == dp[i] - 1:
        i -= 1
    result.append(i)

print(dp[N])
print(*result)

"""
- 난이도: 실버1
- 분류: dp (최적해)
"""
