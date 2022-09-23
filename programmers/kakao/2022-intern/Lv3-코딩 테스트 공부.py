def solution(alp, cop, problems):
    INF = int(1e9)

    # 목표 추출
    target_alp = 0
    target_cop = 0
    for p in problems:
        target_alp = max(target_alp, p[0])
        target_cop = max(target_cop, p[1])

    # 예외처리: 초기값이 목표값보다 클 경우
    if alp >= target_alp:
        alp = target_alp
    if cop >= target_cop:
        cop = target_cop

    # dp[i][j]: 알고력 i, 코딩력 j를 얻는데 걸리는 최소시간
    dp = [[INF] * (target_cop + 1) for _ in range(target_alp + 1)]
    dp[alp][cop] = 0

    for i in range(alp, target_alp + 1):
        for j in range(cop, target_cop + 1):
            # Case1: 알고력 올리기
            ni = i + 1
            if ni > target_alp:
                ni = target_alp
            dp[ni][j] = min(dp[ni][j], dp[i][j] + 1)
            # Case2: 코딩력 올리기
            nj = j + 1
            if nj > target_cop:
                nj = target_cop
            dp[i][nj] = min(dp[i][nj], dp[i][j] + 1)
            # Case3: 문제 풀기
            for p in problems:
                if i >= p[0] and j >= p[1]:
                    ni = i + p[2]
                    nj = j + p[3]
                    if ni > target_alp:
                        ni = target_alp
                    if nj > target_cop:
                        nj = target_cop
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + p[4])
    return dp[target_alp][target_cop]
