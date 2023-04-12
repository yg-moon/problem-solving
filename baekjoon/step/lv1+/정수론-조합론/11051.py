# 이항 계수 2
# 출처: https://pacific-ocean.tistory.com/207
N, K = map(int, input().split())
dp = [[1] * i for i in range(1, 1003)]

for i in range(2, 1002):
    for j in range(i + 1):
        if j == 0 or j == i:
            continue
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[N][K] % 10007)

"""
- 난이도: 실버2
- 분류: 조합론, DP

- 파스칼의 삼각형
"""
