# 앱
N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

sum_cost = sum(cost)

# dp[j]: 비용 j로 확보할 수 있는 최대 메모리
dp = [0] * (sum_cost + 1)

# 1차원 냅색: 현재 비용까지만 역순으로 갱신
for i in range(N):
    for j in range(sum_cost, cost[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - cost[i]] + memory[i])

# M 이상의 메모리를 확보할 수 있는 최소비용을 출력
for j in range(sum_cost + 1):
    if dp[j] >= M:
        print(j)
        break

"""
- 1차원 버전
- 참고: https://hackids.tistory.com/113
"""
