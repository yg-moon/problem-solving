# 이항 계수 2
# 출처: https://pacific-ocean.tistory.com/207
N, K = map(int, input().split())

dp = [[0] for _ in range(1002)]
dp[1].append(1)

for i in range(2, 1002):
    for j in range(1, i + 1):
        if j == 1:
            dp[i].append(1)
        elif j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])

print(dp[N + 1][K + 1] % 10007)

"""
- 난이도: 실버2
- 분류: 조합론, DP

- 파스칼의 삼각형
"""
