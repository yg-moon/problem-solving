# 격자상의 경로
N, M, K = map(int, input().split())

# 핵심1: 동그라미 위치 찾기
if K != 0:
    div, mod = divmod(K, M)
    # 주의: 나머지가 0인 경우 예외처리
    if mod != 0:
        r = div
        c = mod - 1
    else:
        r = div - 1
        c = M - 1
else:
    r = N - 1
    c = M - 1

# dp[i][j]: (i,j)까지 도달할 수 있는 경로의 개수
dp = [[0] * M for _ in range(N)]
# 초기화
dp[0][0] = 1

# 핵심2: 시작점~경유지 경로의 개수 + 경유지~도착점 경로의 개수
for i in range(N):
    for j in range(M):
        if i + 1 <= r:
            dp[i + 1][j] += dp[i][j]  # 아래쪽
        if j + 1 <= c:
            dp[i][j + 1] += dp[i][j]  # 오른쪽

for i in range(r, N):
    for j in range(c, M):
        if i + 1 < N:
            dp[i + 1][j] += dp[i][j]  # 아래쪽
        if j + 1 < M:
            dp[i][j + 1] += dp[i][j]  # 오른쪽

print(dp[N - 1][M - 1])

"""
- 난이도: 실버1
- 분류: dp

- 요약: 경로의 개수를 계산하는 2차원 dp 유형
- 디버깅: divmod 연산시 나머지가 0인 경우 예외처리 하기
"""
