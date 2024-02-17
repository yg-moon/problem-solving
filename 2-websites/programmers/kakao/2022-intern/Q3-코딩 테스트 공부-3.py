def solution(alp, cop, problems):
    # 목표 설정
    target_alp = 0
    target_cop = 0
    for p in problems:
        target_alp = max(target_alp, p[0])
        target_cop = max(target_cop, p[1])

    # 초기값이 목표보다 큰 경우를 위한 처리
    alp = min(alp, target_alp)
    cop = min(cop, target_cop)

    # dp[i][j]: 알고력i, 코딩력j를 얻는데 걸리는 최소시간
    INF = int(1e9)
    dp = [[INF] * 151 for _ in range(151)]
    dp[alp][cop] = 0

    for i in range(alp, target_alp + 1):
        for j in range(cop, target_cop + 1):
            # Case1: 알고력 올리기
            if i + 1 <= target_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            # Case2: 코딩력 올리기
            if j + 1 <= target_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            # Case3: 문제 풀기
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    # 주의: 목표를 넘어가지 않게 처리
                    ni = min(i + alp_rwd, target_alp)
                    nj = min(j + cop_rwd, target_cop)
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + cost)

    return dp[target_alp][target_cop]


"""
- 바텀업 DP 풀이 (정해)

핵심
- dp[i][j]가 아니라 dp[i+1][j], dp[i][j+1] 을 갱신하는 것
- target_alp, target_cop를 넘어갈 경우 값을 재조정 해주는 것
"""
