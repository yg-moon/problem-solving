def solution(alp, cop, problems):
    # 목표 설정
    target_alp = 0
    target_cop = 0
    for p in problems:
        target_alp = max(target_alp, p[0])
        target_cop = max(target_cop, p[1])

    # 의미 주의: dp[i][j]: 알고력 i, 코딩력 j로 시작해서, 목표치에 도달하는데 걸리는 최소시간
    INF = int(1e9)
    dp = [[INF] * 151 for _ in range(151)]

    def dfs(a, c):
        # base case
        if a >= target_alp and c >= target_cop:
            return 0
        # top-down: 값이 있으면 리턴
        if dp[a][c] != INF:
            return dp[a][c]
        # 1. 알고력 늘리기
        if a < target_alp:
            dp[a][c] = min(dp[a][c], dfs(a + 1, c) + 1)
        # 2. 코딩력 늘리기
        if c < target_cop:
            dp[a][c] = min(dp[a][c], dfs(a, c + 1) + 1)
        # 3. 문제 풀기
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if a >= alp_req and c >= cop_req:
                # 주의: 목표를 넘어가지 않게 처리
                na = min(a + alp_rwd, target_alp)
                nc = min(c + cop_rwd, target_cop)
                dp[a][c] = min(dp[a][c], dfs(na, nc) + cost)

        return dp[a][c]

    answer = dfs(alp, cop)

    if answer != INF:
        return answer
    else:
        return -1


"""
- 탑다운 DP 풀이
- 소요 시간
    - 2:55-3:30 (35분) (1차 시도, 예제 시간초과)
    - 7:40-7:55 (15분) (2차 시도, 탑다운 포기)

디버깅
- 문제점: dp 배열의 정의가 틀렸고, 풀이의 진행방향이 반대로 되었음
- 참고: 프로그래머스
"""
