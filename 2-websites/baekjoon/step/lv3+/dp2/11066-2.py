# 파일 합치기
# 출처: GPT4
def dfs(i, j):
    # 이미 방문했으면 리턴
    if dp[i][j] != -1:
        return dp[i][j]

    # 자기 자신의 비용은 0
    if i == j:
        dp[i][j] = 0
        return dp[i][j]

    # top-down 구간 쪼개기
    min_cost = int(1e9)
    for k in range(i, j):
        cost = dfs(i, k) + dfs(k + 1, j) + psum[j] - psum[i - 1]
        min_cost = min(min_cost, cost)

    # 저장하고 리턴
    dp[i][j] = min_cost
    return dp[i][j]


T = int(input())

for _ in range(T):
    K = int(input())
    files = [0] + list(map(int, input().split()))
    psum = [0] * (K + 1)

    for i in range(1, K + 1):
        psum[i] = psum[i - 1] + files[i]

    dp = [[-1] * (K + 1) for _ in range(K + 1)]
    print(dfs(1, K))

"""
- Top down 버전
"""
