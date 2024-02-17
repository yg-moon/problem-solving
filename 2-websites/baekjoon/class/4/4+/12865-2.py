N, K = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(N)]

# dp[j]: 허용무게가 j인 배낭의 최대가치
dp = [0] * (K + 1)

# 1차원: 현재 짐의 무게까지만 역순으로 갱신
for i in range(N):
    w = bags[i][0]
    v = bags[i][1]
    for j in range(K, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[K])

""""
- 간결하고 효율적인 1차원 냅색 (168ms)
- 출처: https://sskl660.tistory.com/88
"""
