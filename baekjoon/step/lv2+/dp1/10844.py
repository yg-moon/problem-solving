# 쉬운 계단 수
# 출처: https://cotak.tistory.com/12
N = int(input())

# 핵심: dp[자리 수][앞에 오는 숫자] = 경우의 수
dp = [[0] * 10 for _ in range(N + 1)]

# 초기화
for i in range(1, 10):
    dp[1][i] = 1

# 핵심
for i in range(2, N + 1):
    for j in range(10):
        # 0: 이전 자리수에서, 앞에 오는 숫자가 1의 경우만 더함
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        # 9: 이전 자리수에서, 앞에 오는 숫자가 8의 경우만 더함
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        # 나머지: 이전 자리수에서, 앞에 오는 숫자가 +/- 1 일때의 두 경우를 더함
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N]) % 1000000000)

"""
- 난이도: 실버1
- 분류: dp

- 아이디어를 잘 찾아서 2차원 dp로 풀어내야 하는 문제
"""
