# 알파벳
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
max_len = 1
visited = set()
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def dfs(x, y, path_len):
    global max_len
    max_len = max(max_len, path_len)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in visited:
            visited.add(board[nx][ny])
            dfs(nx, ny, path_len + 1)
            visited.remove(board[nx][ny])


visited.add(board[0][0])
dfs(0, 0, 1)
print(max_len)

"""
- 난이도: 골드4
- 분류: 백트래킹
"""
