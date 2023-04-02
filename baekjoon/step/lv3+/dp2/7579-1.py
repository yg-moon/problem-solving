# 앱
# 출처: https://claude-u.tistory.com/445
N, M = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
sum_costs = sum(cost)
answer = sum_costs

# dp[i][j]: i번째 앱까지 고려했을때 j의 비용으로 얻을 수 있는 최대 메모리
dp = [[0] * (sum_costs + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    # 주의: j는 cost 배열을 순회하는 인덱스가 아니라, 가능한 비용을 의미하므로 0부터 시작
    for j in range(sum_costs + 1):
        # 1. 앱을 비활성화할 비용이 부족한 경우: 이전 결과를 그대로 사용
        if j < cost[i]:
            dp[i][j] = dp[i - 1][j]
        # 2. 비용이 충분한 경우: max(이전 결과, 현재 앱을 종료했을때 결과)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + memory[i])

        # M 이상의 메모리를 확보할 수 있으면: 최소 비용을 갱신
        if dp[i][j] >= M:
            answer = min(answer, j)

print(answer)

"""
- 난이도: 골드3
- 분류: dp (냅색)

문제 설명에 나온 '발상의 전환'이란?
- M <= 1000만 이므로, dp의 j축을 '메모리'로 잡으면 테이블이 너무 커진다.
- 따라서 dp의 j축을 '비용'으로 잡고, dp값을 '최대 메모리'로 잡아서 해결했다.
- 즉, dp의 축과 배열값의 의미를 잘 결정해야 한다는 의미였다.
"""
