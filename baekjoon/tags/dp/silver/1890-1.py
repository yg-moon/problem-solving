# 점프
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: (i,j)까지 도달할 수 있는 경로의 개수
dp = [[0] * N for _ in range(N)]
# 초기화
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        # 최적화: 어차피 이동할 경로가 없는 곳은 패스
        if dp[i][j] == 0 or graph[i][j] == 0:
            continue
        # 핵심: 범위내에서 이동 가능한 칸에 여태까지 경로의 개수를 더해줌
        if i + graph[i][j] < N:
            dp[i + graph[i][j]][j] += dp[i][j]  # 아래쪽
        if j + graph[i][j] < N:
            dp[i][j + graph[i][j]] += dp[i][j]  # 오른쪽

print(dp[N - 1][N - 1])

"""
- 난이도: 실버1
- 분류: dp

- 요약: 경로의 개수를 계산하는 2차원 dp 유형
- 바텀업 풀이
"""
