# 동전 1
# 출처: https://seongonion.tistory.com/108
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# dp[i]: 모든 동전들을 조합하여 i원을 만들 수 있는 경우의 수
dp = [0] * (k + 1)

# dp[0]: 동전을 하나만 사용하는 경우를 위해 설정 (의미에는 어긋나지만, 구현의 편의성을 위해)
# ex. 동전이 3원일 때, dp[3-3] = 1로 맞춰줌으로써, 0원에서 3원을 더해 3원을 만드는 경우라고 생각
dp[0] = 1

for coin in coins:
    for i in range(coin, k + 1):
        # 핵심: coin원 동전으로 i원 만들기 -> i-coin원을 만든 후 coin원을 추가하는 것과 같음
        # 즉, 기존의 경우에 i-coin원의 경우를 더해주기만 하면 됨
        dp[i] += dp[i - coin]

print(dp[k])

"""
- 난이도: 골드5
- 분류: dp

- 메모리 제한이 4MB이므로, 1차원 배열에서 덮어써가며 풀어야 하는 제약사항이 있음
"""
