# 1, 2, 3 더하기

# dp[i]: i를 1,2,3의 합으로 나타내는 방법의 수
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n])

"""
- 난이도: 실버3
- 분류: dp

- 요약: 항이 3개인 피보나치 수열 문제
- 정답: 정수를 1,2,3의 합으로만 나타내야 하므로, 현재 숫자와 1,2,3씩 차이나는 dp값만 고려
    ex. dp[5] = dp[4] (의 모든 경우에 1씩 더하면 되므로)
                + dp[3] (의 모든 경우에 2씩 더하면 되므로)
                + dp[2] (의 모든 경우에 3씩 더하면 되므로)

- 참고: https://e-you.tistory.com/304
"""
