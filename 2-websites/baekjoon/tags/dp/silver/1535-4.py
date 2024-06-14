N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

# dp[j]: 체력 j로 먹을 수 있는 최대 기쁨
dp = [0] * 101

for i in range(N):
    # 최댓값부터 현재값까지 역순으로 돌면서 처리
    for j in range(100, L[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - L[i]] + J[i])

print(dp[99])

"""
- 1차원 냅색 풀이
"""
