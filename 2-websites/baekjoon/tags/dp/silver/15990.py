# 1, 2, 3 더하기 5
MAX = 1_000_001
MOD = 1_000_000_009

# dp[i][j]: i를 1,2,3의 합으로 나타내는 방법의 수, 마지막에 더한 숫자가 j일때
dp = [[0] * 4 for _ in range(MAX)]
# 초기화
dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

# 핵심: 현재숫자에서 끝자리가 1인건, 현재숫자-1에서 끝자리가 2나 3인 것의 개수의 합
for i in range(4, MAX):
    if i - 1 >= 0:
        dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
    if i - 2 >= 0:
        dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD
    if i - 3 >= 0:
        dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD

T = int(input())

for _ in range(T):
    n = int(input())
    print((dp[n][1] + dp[n][2] + dp[n][3]) % MOD)

"""
- 난이도: 실버2
- 분류: dp

- 요약: 직전 선택지에 영향을 받는 2차원 dp 유형
- 참고: https://jdselectron.tistory.com/71
"""
