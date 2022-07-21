# BOJ 18428
N = int(input())

graph = []
for _ in range(N):
    graph.append(input().split())

WALL = "O"
EMPTY = "X"
STUDENT = "S"
TEACHER = "T"

empty_locs = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == EMPTY:
            empty_locs.append((i, j))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 한쪽만 뚫는 DFS
def dfs(i, x, y):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != WALL:
        if graph[nx][ny] == STUDENT:
            return False
        if graph[nx][ny] == EMPTY:
            # 팁: 이렇게 해야 리턴값을 맨 위로 올릴 수 있음
            return dfs(i, nx, ny)
    return True


def simulate():
    # 3중 for문으로 벽 세우기
    for i in range(len(empty_locs)):
        for j in range(i):
            for k in range(j):
                x1, y1 = empty_locs[i]
                x2, y2 = empty_locs[j]
                x3, y3 = empty_locs[k]

                # 벽 세우기
                graph[x1][y1] = WALL
                graph[x2][y2] = WALL
                graph[x3][y3] = WALL

                # DFS 돌리기
                can_hide = True
                for x in range(N):
                    for y in range(N):
                        if graph[x][y] == TEACHER:
                            for dir in range(4):
                                can_hide = can_hide and dfs(dir, x, y)
                if can_hide:
                    return True

                # 벽 지우기
                graph[x1][y1] = EMPTY
                graph[x2][y2] = EMPTY
                graph[x3][y3] = EMPTY
    return False


if simulate():
    print("YES")
else:
    print("NO")
