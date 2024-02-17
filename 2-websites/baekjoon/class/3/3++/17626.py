# Four Squares
# 출처: https://donghak-dev.tistory.com/49
n = int(input())

# dp[i]: 합이 i와 같게 되는 제곱수들의 최소 개수
dp = [0] * 50001
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    min_val = int(1e9)
    j = 1
    # 핵심: dp[i] = dp[i - (i 이하의 제곱수)]의 최솟값 + 1
    while (j**2) <= i:
        min_val = min(min_val, dp[i - (j**2)])
        j += 1
    dp[i] = min_val + 1

print(dp[n])

"""
- 난이도: 실버3
- 분류: dp

- ex. dp[9] = min(dp[9 - 1^2], dp[9 - 2^2], dp[9 - 3^2]) + 1
            = min(dp[8], dp[5], dp[0]) + 1
            = 0 + 1
            = 1
"""
