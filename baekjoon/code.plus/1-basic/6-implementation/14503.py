# 로봇 청소기
N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]
x, y = r, c
visited = set()
answer = 0
done = False

while not done:
    # 1.현재 위치를 청소
    visited.add((x, y))
    answer += 1
    # 2.(문제 설명대로)
    searching = True
    while searching:
        moved = False
        for _ in range(4):
            nd = (d - 1) % 4
            nx, ny = x + dx[nd], y + dy[nd]
            # 2-1
            if (
                0 <= nx < N
                and 0 < ny < M
                and (nx, ny) not in visited
                and board[nx][ny] == 0
            ):
                x, y, d = nx, ny, nd
                searching = False
                moved = True
                break
            # 2-2
            # 주의: 방향전환은 항상 해주어야 함
            d = nd

        if not moved:
            nx, ny = x - dx[d], y - dy[d]
            # 2-3
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 1:
                x, y = nx, ny
            # 2-4
            else:
                searching = False
                done = True

print(answer)

"""
- 요약: 주어진 그대로 구현
- 구현
    - 적절한 flag 변수들의 사용.
    - 각 문항의 요구사항대로 정확히 구현.
"""
