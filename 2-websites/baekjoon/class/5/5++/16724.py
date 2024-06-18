# 피리 부는 사나이
N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

dir = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
visited = [[0] * M for _ in range(N)]
answer = 0


def dfs(x, y, num):
    global is_new_group

    visited[x][y] = num
    nx = x + dir[graph[x][y]][0]
    ny = y + dir[graph[x][y]][1]

    if visited[nx][ny] == 0:
        dfs(nx, ny, num)
    elif visited[nx][ny] < num:
        is_new_group = False


group_num = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            is_new_group = True
            group_num += 1
            dfs(i, j, group_num)
            if is_new_group:
                answer += 1

print(answer)

"""
- 난이도: 골드3
- 분류: DFS
- 소요 시간: 30분

요약
- DFS로 연결된 집합을 하나씩 찾기
- 집합마다 번호를 붙여서 칠해나가며, 이전에 찾은 집합과 합쳐질 경우에는 정답을 늘리지 않음
"""
