# 평범한 배낭
# 출처: https://sskl660.tistory.com/88
N, K = map(int, input().split())
bags = [[0, 0]]
for _ in range(N):
    W, V = map(int, input().split())
    bags.append((W, V))

# dp[j]: 허용무게가 j인 배낭의 최대가치
dp = [0] * (K + 1)

for i in range(1, N + 1):
    # 1차원 냅색: 현재 짐의 무게까지만 역순으로 갱신
    for j in range(K, bags[i][0] - 1, -1):
        dp[j] = max(dp[j], dp[j - bags[i][0]] + bags[i][1])

print(dp[K])

"""
- 더 효율적인 bottom-up 1차원 냅색
"""
