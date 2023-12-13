# 이동하기
import sys

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: (i,j)까지 이동했을 때 가능한 최대 사탕개수
dp = [[-1] * M for _ in range(N)]
# 초기화
dp[0][0] = graph[0][0]


def solve(x, y):
    if not (0 <= x < N and 0 <= y < M):
        return 0

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = graph[x][y] + max(solve(x, y - 1), solve(x - 1, y), solve(x - 1, y - 1))

    return dp[x][y]


print(solve(N - 1, M - 1))

"""
- 탑다운 풀이
    - 입력이 크면 재귀스택이 터지므로 주의
    - 지금처럼 점화식이 같은 경우에는 바텀업이 나음
"""
