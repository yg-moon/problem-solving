N, M = map(int, input().split())
mat = [list(map(int, input())) for _ in range(N)]

# dp[i][j]: (i,j)까지 고려했을때 가장 큰 정사각형의 한변 길이
dp = [[-1] * M for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(M):
        # 첫번째 행과 열은 자신 그대로
        if i == 0 or j == 0:
            dp[i][j] = mat[i][j]
        # 값이 없는 곳은 0
        elif mat[i][j] == 0:
            dp[i][j] = 0
        # 나머지는 점화식
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        answer = max(answer, dp[i][j])

print(answer * answer)

"""
- 정해: 바텀업 풀이
    - 탑다운과 반대로 (좌, 상, 좌상) 방향을 고려
    - 그다지 직관적이지는 않지만 효율적(17배 빠름)이므로 풀이를 숙지하자
"""
