# LCS 2
# 출처: https://velog.io/@ledcost/백준-9252-파이썬-LCS-2-골드-4-DP
str1 = " " + input()
str2 = " " + input()
dp = [[""] * len(str2) for _ in range(len(str1))]

# LCS 길이뿐만 아니라 문자열 자체를 구하기
for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + str1[i]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

result = dp[-1][-1]
print(len(result))
if result != "":
    print(result)

"""
- 난이도: 골드4
- 분류: dp (LCS)

- (클래스5 문제지만, LCS 공부하는 김에 같이 풀어봄)
"""
