# 출처: 이코테
def edit_dist(str1, str2):
    N = len(str1)
    M = len(str2)

    # 초기화
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][0] = i
    for j in range(1, M + 1):
        dp[0][j] = j

    # 편집 거리 알고리즘
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[N][M]


str1 = input()
str2 = input()
print(edit_dist(str1, str2))
