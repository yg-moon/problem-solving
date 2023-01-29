# 스티커
T = int(input())

for _ in range(T):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    # 예외처리
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    # 초깃값 설정
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for i in range(2, n):
        # dp[0][i]: 0행 i열까지 진행했을 때의 최대 점수
        # dp[1][i]: 1행 i열까지 진행했을 때의 최대 점수
        dp[0][i] += max(dp[0][i - 2], dp[1][i - 2], dp[1][i - 1])
        dp[1][i] += max(dp[0][i - 2], dp[1][i - 2], dp[0][i - 1])

    print(max(dp[0][n - 1], dp[1][n - 1]))

"""
- 난이도: 실버1
- 분류: dp
"""
