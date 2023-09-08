from collections import deque


def solution(n, m, hole):
    graph = [[0] * m for _ in range(n)]
    for a, b in hole:
        graph[a - 1][b - 1] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    visited = [[[False] * m for _ in range(n)] for _ in range(2)]
    visited[0][0][0] = True
    q = deque()
    q.append((0, 0, 0, 0))
    answer = int(1e9)

    while q:
        x, y, time, used = q.popleft()

        if x == n - 1 and y == m - 1:
            answer = min(answer, time)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 신발 사용하지 않고 이동
            # 주의: 기존 사용여부를 그대로 기록
            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[used][nx][ny]
                and graph[nx][ny] == 0
            ):
                visited[used][nx][ny] = True
                q.append((nx, ny, time + 1, used))

            # 신발 사용
            if used == 0:
                nx += dx[i]
                ny += dy[i]
                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and not visited[1][nx][ny]
                    and graph[nx][ny] == 0
                ):
                    visited[1][nx][ny] = True
                    q.append((nx, ny, time + 1, 1))

    return answer if answer != int(1e9) else -1


"""
- 분류: BFS
- 시간: 30분

- 벽 부수고 이동하기 응용 (3차원 BFS)

- 디버깅
    - 문제1: 실행결과가 null이 나옴
    - 원인: break를 써야 하는 곳에 return을 썼음
    - 문제2: 테스트 결과 실패가 나옴
    - 원인: 신발 사용여부의 기록을 제대로 전달하지 않았음
"""
