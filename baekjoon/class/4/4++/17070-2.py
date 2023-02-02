# 파이프 옮기기 1
# 출처: https://backtony.github.io/algorithm/2021-03-02-algorithm-boj-class4-44/
HORI = 0
VERT = 1
DIAG = 2

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def dfs(x, y, dir):
    global answer
    # 목표 도달
    if (x, y) == (N - 1, N - 1):
        answer += 1
        return

    # 현재방향이 가로 or 대각인 경우: 가로 이동
    if dir == HORI or dir == DIAG:
        if y + 1 < N and graph[x][y + 1] == 0:
            dfs(x, y + 1, HORI)

    # 현재방향이 세로 or 대각인 경우: 세로 이동
    if dir == VERT or dir == DIAG:
        if x + 1 < N and graph[x + 1][y] == 0:
            dfs(x + 1, y, VERT)

    # 현재방향이 가로 or 세로 or 대각인 경우: 대각 이동
    if (
        x + 1 < N
        and y + 1 < N
        and graph[x][y + 1] == 0
        and graph[x + 1][y] == 0
        and graph[x + 1][y + 1] == 0
    ):
        dfs(x + 1, y + 1, DIAG)


dfs(0, 1, HORI)

print(answer)

"""
요약
- DFS로 완전탐색
- visited는 따로 관리할 필요가 없음 (주어진 방향 그대로 매번 진행)
- '다음 이동할 방향'에 따라 3가지 경우로 나누어 구현한다. ('현재 방향'을 기준으로 분기하는 것보다 간결함)

배운점
- 완전탐색은 DFS가 BFS보다 더 빠르다.
"""
