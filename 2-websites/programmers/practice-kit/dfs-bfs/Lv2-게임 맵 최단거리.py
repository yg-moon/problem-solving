from collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])
    answer = int(1e9)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = set([(0, 0)])
    q = deque([(0, 0, 1)])

    while q:
        x, y, dist = q.popleft()

        if (x, y) == (N - 1, M - 1):
            answer = min(answer, dist)
            # 주의: 여기에 return 쓰면 틀림

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < M
                and maps[nx][ny] == 1
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                q.append((nx, ny, dist + 1))

    if answer == int(1e9):
        return -1
    return answer


"""
- 기본적인 BFS
"""
