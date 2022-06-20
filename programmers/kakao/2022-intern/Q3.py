# Time Limit Exceeded

import sys
sys.setrecursionlimit(10**7)

def solution(alp, cop, problems):
    # 목표 설정
    alp_target = 0
    cop_target = 0
    for p in problems:
        alp_target = max(alp_target, p[0])
        cop_target = max(cop_target, p[1])

    min_time = sys.maxsize

    def dfs(cur_alp, cur_cop, time):
        if cur_alp >= alp_target and cur_cop >= cop_target:
            nonlocal min_time
            min_time = min(min_time, time)
            return

        dfs(cur_alp + 1, cur_cop, time + 1)
        dfs(cur_alp, cur_cop + 1, time + 1)

        for p in problems:
            if cur_alp >= p[0] and cur_cop >= p[1]:
                dfs(cur_alp + p[2], cur_cop + p[3], time + p[4])

    dfs(alp, cop, 0)

    return min_time


# 가능한 동작
# - 시간 들여서 올리기
# - 문제 풀기

# 목표 alp, 목표, cop
# dfs(현재 alp, 현재 cop, 현재 time)
#   dfs: 시간 올리기 -> alp 1 올리기, cop 1 올리기.
#   dfs: 문제 1풀기
#   dfs: 문제 2풀기

# 조건을 만족할 때 까지 dfs.
# 그때까지의 시간을 기록. (기존의 최솟값보다 작아야 기록)
# 최종적으로 제일 작은 시간을 정답으로.
# ---------------------------------------------
# 핵심: 매번 어떤 전략을 선택해야 하는지
# 그냥 시간을 들여서 올릴수도 있고.
# 문제 푸는게 더 효율적이라면 문제를 풀어서 올릴수도 있고.
# 결국에는 총 시간이 최소가 되도록 전략을 짜야 한다.

# 한 방식이 다른것 보다 오래 걸릴지 어떻게 알지?
# 그리디로 풀 수 있나? 아니면 일단 해보고 기록을 비교하는건가?

# 아이디어
# (그냥 시간을 들여서 올리는 것) vs (시간을 조금 들여서 조건을 만족 + 문제를 푸는)게 총 시간이 빠르면 후자를 선택.
# (문제를 풀어서 조건을 만족하고 다음 문제를 푸는 것) 까지도 고려해야 한다.

# 참고: 문제들의 시간이 너무 비효율적이면 그냥 올리는게 나을수도 있음.
# 그래서 모든 가능성 중에서 가장 작은 경로를 선택해야 한다.

# 해당 문제를 몇번이나 풀고 넘어가는게 가장 최적인지 어떻게 알지?
# 극단적인 경우
# 문제들이 리워드를 주지 않아서 그냥 시간을 올리는게 나은 경우.
# 한 문제에 극단적으로 리워드가 있어서 그거만 만족하고 풀면 되는 경우.

# DFS, 백트래킹?
