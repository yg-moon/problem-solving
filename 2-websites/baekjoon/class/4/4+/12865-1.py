# 평범한 배낭
N, K = map(int, input().split())
bags = [[0, 0]]
for _ in range(N):
    W, V = map(int, input().split())
    bags.append((W, V))

# dp[i][j]: i번째 물건까지 살펴봤을때, 허용무게가 j인 배낭의 최대가치 (1-idx)
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = bags[i][0]
        v = bags[i][1]
        # 1. 현재 물건을 넣을 수 없다면 (배낭의 허용 무게 < 넣을 물건의 무게):
        # - 이전 배낭을 그대로 가지고 감
        if j < w:
            dp[i][j] = dp[i - 1][j]
        # 2. 현재 물건을 넣을 수 있다면, 둘중 가치가 더 높은 쪽을 선택:
        # - 이전 배낭을 그대로 가지고 가는 경우
        # - 현재 물건을 배낭에 넣는 경우
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[N][K])

"""
- 난이도: 골드5
- 분류: dp

- 가장 일반적인 바텀업 2차원 냅색 (360ms)
- 참고: https://hongcoding.tistory.com/50
"""
