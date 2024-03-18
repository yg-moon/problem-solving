# 앱
N, M = map(int, input().split())
memory = [0] + list(map(int, input().split()))  # 1-idx
cost = [0] + list(map(int, input().split()))

# 초기화: 모든 앱을 비활성화 할때 드는 비용
sum_cost = sum(cost)
answer = sum_cost

# dp[i][j]: i번째 앱까지 고려했을때 j의 비용으로 얻을 수 있는 최대 메모리
dp = [[0] * (sum_cost + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(sum_cost + 1):
        # 1. 비활성화할 비용이 부족한 경우: 이전 결과를 그대로 사용
        if j < cost[i]:
            dp[i][j] = dp[i - 1][j]
        # 2. 비활성화가 가능한 경우: max(이전 결과, 비활성화한 결과)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + memory[i])

        # M 이상의 메모리를 확보할 수 있으면, 최소 비용을 갱신
        if dp[i][j] >= M:
            answer = min(answer, j)

print(answer)

"""
- 난이도: 골드3
- 분류: dp
- 유형: 냅색 변형 (축 변경)

문제 설명에 나온 '발상의 전환'이란?
- M <= 1000만 이므로, dp의 j축을 '메모리'로 잡으면 테이블이 너무 커진다.
- 따라서 dp의 j축을 '비용'으로 잡고, dp값을 '최대 메모리'로 잡아서 해결했다.
- 즉, dp의 축과 배열값의 의미를 잘 결정해야 한다는 의미였다.

참고: https://claude-u.tistory.com/445
"""
