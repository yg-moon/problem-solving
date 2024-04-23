N, M = 0, 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[0] * 5 for _ in range(5)]
blocks = [[0] * 5 for _ in range(5)]


def out_of_bounds(x, y):
    return x < 0 or x >= N or y < 0 or y >= M


# ret: 현재 상태에서 최적의 플레이를 할 때 남은 이동횟수
# ret가 짝수: 플레이어가 패배함을 의미 / 홀수: 플레이어가 승리함을 의미
# cur_x, cur_y: 현재 플레이어의 좌표 / op_x, op_y: 상대 플레이어의 좌표
def solve(cur_x, cur_y, op_x, op_y):
    global visited, blocks

    # 플레이어가 밟고 있는 발판이 사라졌다면
    if visited[cur_x][cur_y]:
        return 0

    ret = 0
    # 플레이어를 네 방향으로 이동시켜 다음 단계로 진행
    for dir in range(4):
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]
        if out_of_bounds(nx, ny) or visited[nx][ny] or blocks[nx][ny] == 0:
            continue

        # 방문 표시
        visited[cur_x][cur_y] = 1

        # val: 플레이어를 dir 방향으로 이동시켰을 때 남은 턴의 수
        val = solve(op_x, op_y, nx, ny) + 1

        # 방문 표시 해제
        visited[cur_x][cur_y] = 0

        # 1. 현재 저장된 턴은 패배인데 새로 계산된 턴은 승리인 경우 -> 바로 갱신
        if ret % 2 == 0 and val % 2 == 1:
            ret = val
        # 2. 현재 저장된 턴과 새로 계산된 턴이 모두 패배인 경우 -> 최대한 늦게 지기
        elif ret % 2 == 0 and val % 2 == 0:
            ret = max(ret, val)
        # 3. 현재 저장된 턴과 새로 계산된 턴이 모두 승리인 경우 -> 최대한 빨리 이기기
        elif ret % 2 == 1 and val % 2 == 1:
            ret = min(ret, val)
    return ret


def solution(board, aloc, bloc):
    global N, M

    N = len(board)
    M = len(board[0])

    for i in range(N):
        for j in range(M):
            blocks[i][j] = board[i][j]

    return solve(aloc[0], aloc[1], bloc[0], bloc[1])


"""
- 분류: 백트래킹, 게임 이론
- 출처: https://blog.encrypted.gg/1032

- 사실상 Minimax Tree의 개념을 알아야 했던 만점방지용 문제
"""
