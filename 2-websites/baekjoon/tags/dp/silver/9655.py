# 돌 게임
N = int(input())

# dp[i]: 돌 i개를 최적으로 가져가는데 걸리는 횟수
dp = [0] * 1001
# 초기화
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = min(dp[i - 1], dp[i - 3]) + 1

if dp[N] % 2 == 0:
    print("CY")
else:
    print("SK")

"""
- 난이도: 실버5
- 분류: dp

- 요약: 가장 기본적인 1차원 dp 유형
- 참고: https://beginnerdeveloper-lit.tistory.com/83
"""
