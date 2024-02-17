from collections import deque


def solution(board):
    n = len(board)
    INF = int(1e9)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 핵심: 방향을 고려한 3차원 배열
    visited = [[[INF] * n for _ in range(n)] for _ in range(4)]
    q = deque()

    # 모든 방향에 대해 초기화
    for i in range(4):
        visited[i][0][0] = 0
    q.append((0, 0, -1, 0))

    while q:
        x, y, dir, cost = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                if dir != i and dir != -1:
                    ncost = cost + 600
                else:
                    ncost = cost + 100
                if ncost < visited[i][nx][ny]:
                    q.append((nx, ny, i, ncost))
                    visited[i][nx][ny] = ncost

    # 모든 방향에 대해 최솟값 찾기
    result = INF
    for i in range(4):
        result = min(result, visited[i][n - 1][n - 1])
    return result


"""
- 분류: BFS (3차원)
- 소요 시간: 70분
"""
