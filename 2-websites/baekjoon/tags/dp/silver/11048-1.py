# 이동하기
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: (i,j)까지 이동했을 때 가능한 최대 사탕개수
# 주의: 인덱스 에러 방지를 위해 x, y 한칸씩 패딩
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        # 주의: 패딩을 고려한 인덱스 조절
        dp[i][j] = graph[i - 1][j - 1] + max(
            dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]
        )

print(dp[N][M])

"""
- 난이도: 실버2
- 분류: dp

- 요약: 진행방향을 역으로 생각하는 2차원 dp 유형 (바텀업 풀이)
- 핵심: (우/하/우+하)로 이동할 수 있으므로, 역으로 (좌/상/좌+상)에서 들어오는 값을 생각
"""
