# 정수 삼각형
N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))

# dp[i][j]: 삼각형에서 i행 j열까지 진행했을 때의 최대값
for i in range(1, N):
    for j in range(i + 1):
        # 맨 왼쪽의 경우: 위쪽만 더함
        if j == 0:
            dp[i][j] += dp[i - 1][j]
        # 맨 오른쪽의 경우: 왼쪽 위만 더함
        elif j == i:
            dp[i][j] += dp[i - 1][j - 1]
        # 나머지 경우: max(위쪽, 왼쪽 위)를 더함
        else:
            dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1])

# 정답: 마지막 행의 최댓값
print(max(dp[N - 1]))

"""
- 난이도: 실버1
- 분류: dp
"""
