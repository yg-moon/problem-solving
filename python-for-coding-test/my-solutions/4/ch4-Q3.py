n, m = map(int, input().split())
a, b, d = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]
game_map[a][b] = 2  # 방문했다는 표시
count = 1 # 방문 횟수

# 왼쪽으로 회전
def turn_left(d: int):
    if d == 0:
        return 3
    return d - 1

while True:
    moved = False
    for _ in range(4):
        d = turn_left(d)
        na = a + dx[d]
        nb = b + dy[d]
        if game_map[na][nb] == 0:
            game_map[na][nb] = 2
            a = na
            b = nb
            count += 1
            moved = True
            break

    if not moved:
        na = a - dx[d]
        nb = b - dy[d]
        # 뒤로 방문할 수 없는 경우 게임종료
        if game_map[na][nb] != 0:
            break
        # 뒤로 가기
        a = na
        b = nb

print(count)
