# 주사위 굴리기
# 출처: https://hongcoding.tistory.com/128
N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmds = list(map(int, input().split()))
dirs = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]  # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
dice = [0, 0, 0, 0, 0, 0]  # 상, 하, 좌, 우, 앞, 뒤


def roll(cmd):
    global dice
    a, b, c, d, e, f = dice
    if cmd == 1:
        dice = [c, d, b, a, e, f]
    elif cmd == 2:
        dice = [d, c, a, b, e, f]
    elif cmd == 3:
        dice = [e, f, c, d, b, a]
    elif cmd == 4:
        dice = [f, e, c, d, a, b]


for cmd in cmds:
    nx, ny = x + dirs[cmd][0], y + dirs[cmd][1]
    if 0 <= nx < N and 0 <= ny < M:
        roll(cmd)
        if board[nx][ny] == 0:
            board[nx][ny] = dice[1]
        else:
            dice[1] = board[nx][ny]
            board[nx][ny] = 0
        print(dice[0])
        x, y = nx, ny

"""
- 주사위를 굴린 방향에 따라 상/하/좌/우/앞/뒤가 바뀌는 규칙만 찾으면 된다.
"""
