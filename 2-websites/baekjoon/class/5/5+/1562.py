# 계단 수
N = int(input())

MOD = 1_000_000_000
MAX_BIT = (1 << 10) - 1

# dp[자리 수][마지막 숫자][사용된 숫자들의 비트]
# ex. 123 -> 0000001110
dp = [[[0] * (MAX_BIT + 1) for _ in range(10)] for _ in range(N + 1)]

# 초기화: 길이가 1인 경우
for i in range(1, 10):
    dp[1][i][1 << i] = 1

for i in range(2, N + 1):
    for j in range(10):
        for k in range(MAX_BIT + 1):
            # 마지막 숫자가 0보다 크면 해당 숫자보다 1작은 숫자들이 올 수 있음
            if j > 0:
                bit = k | 1 << (j - 1)
                dp[i][j - 1][bit] += dp[i - 1][j][k]
                dp[i][j - 1][bit] %= MOD
            # 마지막 숫자가 9보다 작으면 해당 숫자보다 1큰 숫자들이 올 수 있음
            if j < 9:
                bit = k | 1 << (j + 1)
                dp[i][j + 1][bit] += dp[i - 1][j][k]
                dp[i][j + 1][bit] %= MOD

answer = 0
for i in range(10):
    answer += dp[N][i][MAX_BIT]
    answer %= MOD
print(answer)

"""
- 난이도: 골드1
- 분류: dp + 비트마스킹

- 참고: https://c4u-rdav.tistory.com/84
"""
