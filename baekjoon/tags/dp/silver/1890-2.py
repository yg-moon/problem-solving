# 점프
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: (i,j)에서 '출발'했을때 목적지까지 가는 경로의 개수
dp = [[-1] * N for _ in range(N)]


def dfs(x, y):
    # base case
    if x == N - 1 and y == N - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    # 방문표시 및 초기화
    dp[x][y] = 0

    # 아래로 이동
    if x + graph[x][y] < N:
        dp[x][y] += dfs(x + graph[x][y], y)

    # 오른쪽으로 이동
    if y + graph[x][y] < N:
        dp[x][y] += dfs(x, y + graph[x][y])

    return dp[x][y]


print(dfs(0, 0))

"""
- DFS+DP 풀이

기본 구조
- dp[x][y] = 0 으로 방문표시 및 초기화
- dp[x][y] += dfs(nx, ny) 방식으로 값을 더해줌
- (0,0)에서 시작

주의 사항
- dp 배열 의미가 반대임
- dp 배열 초기화는 추가로 하지 않음
- base case가 중요함
"""
