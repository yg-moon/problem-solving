from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    min_dist = int(1e9)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = set([(0, 0)])
    q = deque([(0, 0, 1)])

    while q:
        x, y, dist = q.popleft()
        if (x, y) == (n - 1, m - 1):
            min_dist = min(min_dist, dist)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and maps[nx][ny] == 1
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                q.append((nx, ny, dist + 1))

    if min_dist == int(1e9):
        return -1
    return min_dist


"""
- 기본적인 BFS
"""
