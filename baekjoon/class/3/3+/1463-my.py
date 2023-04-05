# 1로 만들기
INF = int(1e9)

N = int(input())

# dp[i]: N을 i로 만드는데 필요한 연산의 최소 횟수
dp = [INF] * (N + 1)
dp[N] = 0

# N부터 1까지 내려가면서 dp를 갱신
for i in range(N, 0, -1):
    dp[i - 1] = min(dp[i - 1], dp[i] + 1)
    if i % 2 == 0:
        dp[i // 2] = min(dp[i // 2], dp[i] + 1)
    if i % 3 == 0:
        dp[i // 3] = min(dp[i // 3], dp[i] + 1)

print(dp[1])

"""
- 난이도: 실버3
- 분류: dp
"""
