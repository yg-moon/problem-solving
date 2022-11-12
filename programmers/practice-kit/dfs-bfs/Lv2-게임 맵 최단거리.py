from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    min_dist = int(1e9)

    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]

    visited = set([(0, 0)])
    q = deque([(0, 0, 1)])  # (x, y, cnt)

    while q:
        x, y, cnt = q.popleft()

        if (x, y) == (n - 1, m - 1):
            min_dist = min(min_dist, cnt)

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and maps[nx][ny] == 1
                and (nx, ny) not in visited
            ):
                q.append((nx, ny, cnt + 1))
                visited.add((nx, ny))

    if min_dist == int(1e9):
        return -1
    return min_dist


"""
- 가장 기본적인 BFS
"""
