# 계단 오르기
N = int(input())
arr = [int(input()) for _ in range(N)]

if N <= 2:  # 예외처리
    print(sum(arr))
else:
    # dp[i]: i번째 계단까지 올라갔을때 가능한 최대 점수
    dp = [0] * 300
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

    # 핵심: 점화식
    for i in range(3, N):
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])

    print(dp[N - 1])

"""
- 난이도: 실버3
- 분류: dp
"""
