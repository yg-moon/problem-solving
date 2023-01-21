# LCS
# 출처: https://velog.io/@piopiop/백준-9251-LCS-파이썬
str1 = " " + input()  # 팁: 맨 앞에 공백을 추가하여 구현을 편하게 만듦
str2 = " " + input()
dp = [[0] * len(str2) for _ in range(len(str1))]

# dp[i][j]: X의 i번째, Y의 j번째 글자까지 LCS의 길이
for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])

# 번외: 길이가 아니라 실제 LCS 문자열 구하기
# LCS = ""
# cur_len = 0
# for i, row in enumerate(dp):
#     if row[-1] > cur_len:
#         cur_len = row[-1]
#         LCS += str1[i]
# print(LCS)

"""
- 난이도: 골드5
- 분류: dp (LCS)
"""
