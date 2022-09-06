# BOJ 18405
# 시간 초과 (BFS가 아닌 DFS 완전탐색이기 때문)
from copy import deepcopy

N, K = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def spread(x, y, virus):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
            graph[nx][ny] = virus


for _ in range(S):
    new_mat = deepcopy(graph)
    for virus_num in range(1, K + 1):
        for x in range(N):
            for y in range(N):
                if new_mat[x][y] == virus_num:
                    spread(x, y, virus_num)

print(graph[X - 1][Y - 1])
