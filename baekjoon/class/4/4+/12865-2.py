# 평범한 배낭
# 출처: https://ji-gwang.tistory.com/m/435
N, K = map(int, input().split())
bags = [tuple(map(int, input().split())) for _ in range(N)]

# Top-down 방식이라 dp[i][j]는 별 의미없고, dp[0][0]에 정답이 저장됨
# 굳이 표현하자면 dp[i][j]: i번째 물건부터 사용해서, 무게 j이하로 구성 가능한 최대가치
dp = [[-1] * (K + 1) for _ in range(N + 1)]


def dfs(depth, weight):
    # 무게 초과
    if weight > K:
        return -int(1e9)
    # 개수 초과
    if depth == N:
        return 0

    # 이미 계산한 경우라면 그대로 리턴 (Top-down)
    if dp[depth][weight] != -1:
        return dp[depth][weight]

    # 점화식: max(다음 물건을 넣었을 때 가치, 안 넣었을 때 가치)
    dp[depth][weight] = max(
        dfs(depth + 1, weight + bags[depth][0]) + bags[depth][1], dfs(depth + 1, weight)
    )
    # 저장한 dp값을 리턴 (Top-down)
    return dp[depth][weight]


print(dfs(0, 0))

"""
- 냅색 Top-down 버전
"""
