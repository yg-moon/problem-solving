# RGB 거리
# 출처: https://pacific-ocean.tistory.com/147
N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    # dp[i][0]: i번째 집을 빨강(R)으로 칠했을 때의 최솟값
    # dp[i][1]: i번째 집을 초록(G)으로 칠했을 때의 최솟값
    # dp[i][2]: i번째 집을 파랑(B)으로 칠했을 때의 최솟값
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]

print(min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))

"""
- 난이도: 실버1
- 분류: dp

느낀점
- 주어진 데이터가 2차원이면, 일단 2차원 dp를 시도해보자.
- 이번 문제처럼 주어진 데이터에 덮어쓸 수 있는 풀이는 덮어쓰자.
"""
