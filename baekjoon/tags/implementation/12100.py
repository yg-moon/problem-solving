# 2048 (Easy)
import sys, copy

sys.setrecursionlimit(10**5)

N = int(input())
og_graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0


def get_max(graph):
    ret = 0
    for row in graph:
        ret = max(ret, max(row))
    return ret


def move_util(x, y, graph, dir, merged):
    if graph[x][y] != 0:
        nx = x + dx[dir]
        ny = y + dy[dir]
        # 해당 방향으로 끝까지 움직이기
        while 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]  # swap
            x, y = nx, ny
            nx += dx[dir]
            ny += dy[dir]
        # 같을 경우 합치기
        if (
            0 <= nx < N
            and 0 <= ny < N
            and graph[x][y] == graph[nx][ny]
            and merged[nx][ny] == 0
        ):
            graph[x][y] = 0
            graph[nx][ny] *= 2
            merged[nx][ny] = 1


def move(graph, dir):
    # 연속 합치기 방지
    merged = [[0] * N for _ in range(N)]

    # 상: 1행부터
    if dir == 0:
        for x in range(N):
            for y in range(N):
                move_util(x, y, graph, dir, merged)

    # 하: N행부터
    elif dir == 1:
        for x in range(N - 1, -1, -1):
            for y in range(N):
                move_util(x, y, graph, dir, merged)

    # 좌: 1열부터
    elif dir == 2:
        for y in range(N):
            for x in range(N):
                move_util(x, y, graph, dir, merged)

    # 우: N열부터
    elif dir == 3:
        for y in range(N - 1, -1, -1):
            for x in range(N):
                move_util(x, y, graph, dir, merged)

    return graph


def dfs(graph, depth):
    global answer
    answer = max(answer, get_max(graph))

    if depth >= 5:
        return

    for i in range(4):
        nxt_graph = move(copy.deepcopy(graph), i)
        dfs(nxt_graph, depth + 1)


dfs(og_graph, 0)

print(answer)

"""
- 난이도: 골드2
- 분류: 시뮬레이션, 백트래킹
- 소요 시간: 80분 (풀이 40분, 디버깅 40분)

요약
- 현재 상태를 상하좌우로 움직이는 깊이 5짜리 백트래킹

핵심: 블록 움직임 구현
- 1. 0이 아닌 블록은 해당 방향으로 끝까지 움직이고, 같을 경우 합치기 (단, 연속 합치기x)
- 2. 움직이는 방향에 따라서 먼저 움직이는 블럭의 순서가 다름

디버깅: 틀렸습니다
- 1. deepcopy 해주기
- 2. 루프 안에서 x,y를 직접 변경하지 말고 복사해서 사용하기

테스트 예제
3
2 2 2
2 0 2
2 2 2
"""
