from collections import defaultdict, deque

N = int(input())
K = int(input())

apple = []
for _ in range(K):
    x, y = map(int, input().split())
    apple.append((x, y))

# 방향전환 정보: dict를 이용하여 탐색시간 단축
change_dir = defaultdict(str)
L = int(input())
for _ in range(L):
    time, dir = input().split()
    change_dir[int(time)] = dir

# 맵 그리기: 벽으로 한칸 패딩
P = N + 2
mat = [[0] * P for _ in range(P)]
for i in range(P):
    for j in range(P):
        if i == 0 or i == P - 1 or j == 0 or j == P - 1:
            mat[i][j] = 2  # 벽: 2
mat[1][1] = 1  # 뱀: 1
for x, y in apple:
    mat[x][y] = 3  # 사과: 3

# 방향: right, down, left, up
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 게임 진행
time = 0
x, y = 1, 1
dir = 0
tail = deque()

while True:
    time += 1
    tail.append((x, y)) # 현재 꼬리위치 저장
    nx = x + dx[dir]
    ny = y + dy[dir]
    next = mat[nx][ny]

    # 벽이나 자기 몸에 부딪히면 게임 종료
    if next == 2 or next == 1:
        break

    # 일단 머리를 다음 칸에 위치
    mat[nx][ny] = 1

    # 다음 칸이 비어있는 경우 꼬리 이동 (이전 꼬리 삭제)
    if next == 0:
        tail_x, tail_y = tail.popleft()
        mat[tail_x][tail_y] = 0

    # 머리 이동
    x, y = nx, ny

    # 방향 전환
    if time in change_dir:
        if change_dir[time] == "D":
            dir = (dir + 1) % 4
        elif change_dir[time] == "L":
            dir = (dir - 1) % 4

print(time)
