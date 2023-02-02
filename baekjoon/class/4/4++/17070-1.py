# 파이프 옮기기 1
# 출처: https://backtony.github.io/algorithm/2021-03-02-algorithm-boj-class4-44/
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# dp[d][i][j]: d방향으로 (i,j)까지 진행했을때 가능한 최대 방법의 수
# 방향: 0은 가로, 1은 세로, 2는 대각
dp = [[[0] * N for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1  # 시작 위치

# 초기화
for j in range(2, N):
    if graph[0][j] == 0:
        dp[0][0][j] = dp[0][0][j - 1]

# 배열 채우기
for i in range(1, N):
    for j in range(1, N):
        # 현재방향이 대각일 경우 계산
        if graph[i][j] == 0 and graph[i][j - 1] == 0 and graph[i - 1][j] == 0:
            dp[2][i][j] = (
                dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]
            )
        if graph[i][j] == 0:
            # 현재방향이 가로일 경우 계산
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            # 현재방향이 세로일 경우 계산
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

print(sum(dp[i][N - 1][N - 1] for i in range(3)))

"""
- 난이도: 골드5
- 분류: dp / DFS

요약
- dp를 통한 완전탐색: 3차원 배열을 통해 파이프의 방향마다 가능한 모든 경우를 기록한다.
- 배열 채우기: 첫 행을 채우고, 나머지는 현재방향에 따라 이전 경로에서 들어올 수 있는 모든 값을 더해준다.
    - 핵심: 진행방향의 역순으로 생각하기
    - (주어진 그림을 보면 더 이해하기 쉬움)
    - (고득점kit '등굣길'과 비슷한 풀이)
"""
