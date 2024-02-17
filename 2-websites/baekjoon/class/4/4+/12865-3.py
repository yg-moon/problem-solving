N, K = map(int, input().split())
bags = [[0, 0]]
for _ in range(N):
    W, V = map(int, input().split())
    bags.append((W, V))

# dp[i][j]: i번째 물건까지 살펴봤을때, 허용무게가 j인 배낭의 최대가치 (1-idx)
dp = [[-1] * (K + 1) for _ in range(N + 1)]


def dfs(i, j):
    # base case
    if i == 0 or j == 0:
        return 0

    # top-down
    if dp[i][j] != -1:
        return dp[i][j]

    w = bags[i][0]
    v = bags[i][1]

    # 1. 새로운 물건을 넣지 않는 경우
    if j < w:
        dp[i][j] = dfs(i - 1, j)
    # 2. 새로운 물건을 넣는 경우
    else:
        dp[i][j] = max(dfs(i - 1, j), dfs(i - 1, j - w) + v)

    return dp[i][j]


print(dfs(N, K))

"""
- (N,K)에서 시작하는 Top-down DP (636ms)
- 참고: https://cme10575.tistory.com/99
"""
