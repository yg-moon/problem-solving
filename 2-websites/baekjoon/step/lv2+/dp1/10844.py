# 쉬운 계단 수
N = int(input())

# dp[i][j]: 길이가 i, 끝자리가 j인 계단 수의 개수
dp = [[0] * 10 for _ in range(N + 1)]
MOD = 1_000_000_000

# 초기화
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        # 현재 끝자리가 0: 이전 길이에서 끝자리가 1인 경우만 더함
        if j == 0:
            dp[i][j] = dp[i - 1][1] % MOD
        # 현재 끝자리가 9: 이전 길이에서 끝자리가 8인 경우만 더함 (주의: 0인 경우는 안됨)
        elif j == 9:
            dp[i][j] = dp[i - 1][8] % MOD
        # 나머지: 이전 길이에서 끝자리가 +/- 1 일때의 두 경우를 더함
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD

print(sum(dp[N]) % MOD)

"""
- 난이도: 실버1
- 분류: dp

- 요약: 규칙을 찾는 2차원 dp
- 참고: https://cotak.tistory.com/12
"""
