# GPT의 개선버전
N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]
x, y = r, c
visited = set()
visited.add((x, y))  # 시작 위치 방문 처리
answer = 1  # 첫 청소 시작점 포함

while True:
    cleaned = False

    # 4방향 회전하면서 탐색
    for _ in range(4):
        d = (d - 1) % 4  # 왼쪽으로 회전
        nx, ny = x + dx[d], y + dy[d]

        # 청소되지 않은 공간이 있는 경우
        if (
            0 <= nx < N
            and 0 <= ny < M
            and (nx, ny) not in visited
            and board[nx][ny] == 0
        ):
            visited.add((nx, ny))  # 방문 처리
            x, y = nx, ny
            answer += 1
            cleaned = True
            break

    # 4방향 모두 청소할 수 없을 때
    if not cleaned:
        # 뒤로 이동
        nx, ny = x - dx[d], y - dy[d]

        # 뒤가 벽이면 종료
        if board[nx][ny] == 1:
            break

        # 벽이 아니면 뒤로 이동
        x, y = nx, ny

print(answer)
