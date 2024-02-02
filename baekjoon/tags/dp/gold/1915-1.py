# 가장 큰 정사각형
import sys

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
mat = [list(map(int, input())) for _ in range(N)]

# dp[i][j]: (i,j)에서 시작하는 가장 큰 정사각형 한 변의 길이
dp = [[-1] * M for _ in range(N)]


def dfs(x, y):
    # base case
    if x >= N or y >= M:
        return 0

    # 방문한적 있으면 그대로 리턴
    if dp[x][y] != -1:
        return dp[x][y]

    # 점화식
    dp[x][y] = mat[x][y] + min(dfs(x + 1, y), dfs(x, y + 1), dfs(x + 1, y + 1))

    # 해당없는 자리면
    if mat[x][y] == 0:
        dp[x][y] = 0

    return dp[x][y]


dfs(0, 0)

answer = 0
for row in dp:
    answer = max(answer, max(row))
print(answer * answer)

"""
- 난이도: 골드4
- 분류: dp
- 소요 시간: 60분 (풀이 40분, 디버깅 20분)

- 요약: 인접한 방향(우, 하, 우하)을 고려하는 2차원 dp 유형 (탑다운 풀이)

디버깅: 90% 틀렸습니다
- 원인: base case를 잘못짜서, 입력이 한줄인 경우에 결과가 이상했음
"""
