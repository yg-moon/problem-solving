# 앱
# 출처: https://hackids.tistory.com/113
N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

sum_costs = sum(cost)

# dp[j]: 비용 j로 확보할 수 있는 최대 메모리
dp = [0] * (sum_costs + 1)

# 1차원 냅색: 현재 비용까지만 역순으로 갱신
for i in range(N):
    for j in range(sum_costs, cost[i] - 1, -1):
        # max(그냥 두는 경우, 비활성화 하는 경우)
        dp[j] = max(dp[j], dp[j - cost[i]] + memory[i])

# M 이상의 메모리를 확보할 수 있는 최소비용을 출력
for i in range(sum_costs + 1):
    if dp[i] >= M:
        print(i)
        break

"""
- 1차원 냅색 버전
"""
