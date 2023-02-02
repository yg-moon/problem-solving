# 연구소
from itertools import combinations
from copy import deepcopy

EMPTY = 0
WALL = 1
VIRUS = 2

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

# 매번 새로 그릴 그래프
new_graph = []

# 0의 위치
zero_pos = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            zero_pos.append((i, j))

# 벽 3개 조합
combs = list(combinations(zero_pos, 3))


# DFS: 현재 위치에서 사방을 탐색하고, EMPTY인 칸을 만나면 VIRUS로 칠하고, 그 칸에서 다시 재귀
def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and new_graph[nx][ny] == EMPTY:
            new_graph[nx][ny] = VIRUS
            dfs(nx, ny)


# 현재 벽 조합의 점수 계산
def calc_score(comb):
    # 벽 세우기
    for c in comb:
        new_graph[c[0]][c[1]] = WALL
    # DFS
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == VIRUS:
                dfs(i, j)
    # 0의 개수 세기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == EMPTY:
                cnt += 1
    return cnt


# 모든 조합에 대해 최댓값 찾기
for comb in combs:
    new_graph = deepcopy(graph)  # 지도를 매번 처음 상태로 초기화
    answer = max(answer, calc_score(comb))
print(answer)

"""
- 난이도: 골드4
- 분류: DFS/BFS

버전1
- 탐색: DFS
- 벽 세우기: combinations
- 성능: 1120ms
"""
