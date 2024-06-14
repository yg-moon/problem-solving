N = int(input())
L = [0] + list(map(int, input().split()))  # 1-idx (점화식에 i-1이 들어가므로)
J = [0] + list(map(int, input().split()))

# dp[i][j]: i번째 사람까지 고려했을 때 체력 j로 얻을 수 있는 최대 기쁨
dp = [[0] * 101 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 101):
        # 코스트를 감당할 수 있으면: max(이전값 그대로 vs 현재 경우 추가)
        if L[i] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - L[i]] + J[i])
        # 안 되면: 이전값 그대로
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][99])

"""
- 2차원 냅색 풀이
"""
