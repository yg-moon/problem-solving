# 톱니바퀴 (2)
T = int(input())
gears = [0] + [list(map(int, list(input()))) for _ in range(T)]  # 1-index
K = int(input())
cmds = [list(map(int, input().split())) for _ in range(K)]


# 톱니바퀴 하나를 회전
def rotate(gear, dir):
    new_gear = [0] * 8
    for i in range(8):
        new_gear[(i + dir) % 8] = gear[i]
    return new_gear


# 시작점부터 왼쪽으로 진행
def check_left(cmd):
    target, dir = cmd
    num_and_dir = set()
    cur = target
    cur_dir = dir
    while True:
        if cur == 1:
            break
        if gears[cur][6] != gears[cur - 1][2]:
            num_and_dir.add((cur, cur_dir))
            num_and_dir.add((cur - 1, -cur_dir))
            cur -= 1
            cur_dir *= -1
        else:
            break
    return num_and_dir


# 시작점부터 오른쪽으로 진행
def check_right(cmd):
    target, dir = cmd
    num_and_dir = set()
    cur = target
    cur_dir = dir
    while True:
        if cur == T:
            break
        if gears[cur][2] != gears[cur + 1][6]:
            num_and_dir.add((cur, cur_dir))
            num_and_dir.add((cur + 1, -cur_dir))
            cur += 1
            cur_dir *= -1
        else:
            break
    return num_and_dir


# 모든 톱니바퀴를 회전
def run_cmd(gears, cmd):
    new_gears = gears[:]
    # 주의: 일단 자기 자신은 무조건 돌려야 함!
    gears_to_rotate = set([(cmd[0], cmd[1])])  # {[톱니번호1, 방향1], ...}
    # 입력값이 처음 톱니바퀴가 아닐때만 왼쪽으로 진행
    if cmd[0] != 1:
        gears_to_rotate.update(check_left(cmd))
    # 입력값이 마지막 톱니바퀴가 아닐때만 오른쪽으로 진행
    if cmd[0] != T:
        gears_to_rotate.update(check_right(cmd))
    for num, dir in gears_to_rotate:
        new_gears[num] = rotate(gears[num], dir)
    return new_gears


for cmd in cmds:
    gears = run_cmd(gears, cmd)

answer = 0
for i in range(1, T + 1):
    if gears[i][0] == 1:
        answer += 1
print(answer)

"""
- 요약: 주어진 그대로 구현
- 구현
    - 시작점부터 왼쪽, 오른쪽으로 쭉 진행하며 돌려야 할 톱니바퀴의 번호와 방향을 구한다.
    - 해당 정보를 이용해 모든 톱니바퀴를 회전시키고 다음 명령도 같은 방식으로 수행.
"""
