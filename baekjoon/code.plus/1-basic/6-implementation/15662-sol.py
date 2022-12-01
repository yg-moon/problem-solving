# 톱니바퀴 (2)
from collections import deque

T = int(input())
gears = [0] + [deque(map(int, input())) for _ in range(T)]
K = int(input())
cmds = [list(map(int, input().split())) for _ in range(K)]


def rotate_gears(gear_num, dir):
    global cur_left, cur_right
    # 왼쪽의 톱니바퀴 회전
    cur_dir = dir
    for i in reversed(range(1, gear_num)):
        if gears[i][2] != cur_left:
            cur_left = gears[i][6]
            gears[i].rotate(cur_dir * -1)
            cur_dir *= -1
        else:
            break
    # 오른쪽의 톱니바퀴 회전
    cur_dir = dir
    for i in range(gear_num + 1, T + 1):
        if gears[i][6] != cur_right:
            cur_right = gears[i][2]
            gears[i].rotate(cur_dir * -1)
            cur_dir *= -1
        else:
            break


for gear_num, dir in cmds:
    cur_left, cur_right = gears[gear_num][6], gears[gear_num][2]
    gears[gear_num].rotate(dir)
    rotate_gears(gear_num, dir)

answer = 0
for i in range(1, T + 1):
    if gears[i][0] == 1:
        answer += 1
print(answer)

"""
출처: https://velog.io/@i_am_developer/백준python15662-톱니바퀴2
"""
