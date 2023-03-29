# 평범한 배낭
# 출처: https://cme10575.tistory.com/99
N, K = map(int, input().split())
bags = [[0, 0]]
for _ in range(N):
    W, V = map(int, input().split())
    bags.append((W, V))

# dp[i][j]: i번째 물건까지 살펴봤을때, 허용무게가 j인 배낭의 최대가치
# 주의: 첫 행과 첫 열은 0으로 초기화
dp = [[0] + [-1] * K for _ in range(N + 1)]
dp[0] = [0] * (K + 1)


def dfs(n, w):
    # base case
    if n == 0 or w == 0:
        return dp[n][w]

    # 이미 계산한 경우 그대로 리턴
    if dp[n][w] != -1:
        return dp[n][w]

    # 배낭한계보다 물건이 무거우면: 이전 배낭을 그대로 들고감
    if w < bags[n][0]:
        dp[n][w] = dfs(n - 1, w)
        return dp[n][w]

    # 나머지 경우(물건을 넣을 여유가 되면): 점화식에 따라 dp값을 저장하고 리턴
    # 점화식: max(이전 배낭 그대로 들고가기, 현재 물건 넣기)
    dp[n][w] = max(dfs(n - 1, w), dfs(n - 1, w - bags[n][0]) + bags[n][1])
    return dp[n][w]


print(dfs(N, K))

"""
- (N,K)에서 시작하는 Top-down 냅색
"""
