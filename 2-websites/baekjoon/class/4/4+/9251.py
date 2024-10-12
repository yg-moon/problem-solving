# LCS
str1 = input()
str2 = input()
M = len(str1)
N = len(str2)

# dp[i][j]: X의 i번째, Y의 j번째 글자까지 LCS의 길이
dp = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(1, M + 1):
    for j in range(1, N + 1):
        # 현재 글자가 같으면, 이전 공통결과 + 1
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        # 다르면, 이전 각자결과중 큰 것
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[M][N])

"""
- 난이도: 골드5
- 분류: dp
"""
