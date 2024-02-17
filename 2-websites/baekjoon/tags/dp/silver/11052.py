# 카드 구매하기
N = int(input())

# dp[i]: 카드 i개를 구매하는데 필요한 최대 금액
dp = [0] + list(map(int, input().split()))

for i in range(2, N + 1):
    for j in range(i):
        dp[i] = max(dp[i], dp[i - j] + dp[j])

print(dp[N])

"""
- 난이도: 실버1
- 분류: dp

- 요약: 가능한 모든 경우들을 갱신하는 1차원 dp 유형
"""
