def solution(alp, cop, problems):
    # 목표 설정
    target_alp = 0
    target_cop = 0
    for p in problems:
        target_alp = max(target_alp, p[0])
        target_cop = max(target_cop, p[1])

    answer = 300

    def dfs(alp, cop, time):
        nonlocal answer

        # 이미 최소시간을 넘었으면 조기종료
        if time > answer:
            return

        # 목표를 달성했으면 정답 갱신
        if alp >= target_alp and cop >= target_cop:
            answer = min(answer, time)
            return

        # 1. 문제 풀기
        for problem in problems:
            alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
            if alp >= alp_req and cop >= cop_req:
                dfs(alp + alp_rwd, cop + cop_rwd, time + cost)
        # 2. 코딩력 올리기
        dfs(alp, cop + 1, time + 1)
        # 3. 알고력 올리기
        dfs(alp + 1, cop, time + 1)

    dfs(alp, cop, 0)

    return answer


"""
- 백트래킹 풀이 (정확성 100점, 효율성 0점)
- 소요 시간: 2:30-2:55 (25분)
"""
