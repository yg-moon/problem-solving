# BOJ 14502
from itertools import combinations
from copy import deepcopy

EMPTY = 0
WALL = 1
VIRUS = 2

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

zero_pos = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            zero_pos.append((i, j))

# 벽 3개 좌표 조합
combs = list(combinations(zero_pos, 3))

# 매번 벽을 새로 그릴 matrix
new_graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# DFS: 현재 위치에서 사방을 탐색 → EMPTY인 칸을 만나면 VIRUS로 칠하기 → 그 칸에서 재귀
def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if new_graph[nx][ny] == EMPTY:
                new_graph[nx][ny] = VIRUS
                dfs(nx, ny)


def count_safe_zone(comb):
    # 벽 세우기
    for c in comb:
        new_graph[c[0]][c[1]] = WALL
    # DFS
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == VIRUS:
                dfs(i, j)
    # 0 개수 세기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == EMPTY:
                cnt += 1
    return cnt


max_cnt = 0
for comb in combs:
    new_graph = deepcopy(graph)  # 지도를 매번 처음 상태로 초기화
    max_cnt = max(max_cnt, count_safe_zone(comb))
print(max_cnt)
