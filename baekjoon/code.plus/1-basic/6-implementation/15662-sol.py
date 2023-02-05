# 톱니바퀴 (2)
# 출처: https://velog.io/@i_am_developer/백준python15662-톱니바퀴2
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


for num, dir in cmds:
    cur_left, cur_right = gears[num][6], gears[num][2]
    gears[num].rotate(dir)
    rotate_gears(num, dir)

answer = 0
for i in range(1, T + 1):
    if gears[i][0] == 1:
        answer += 1
print(answer)

"""
- 구현
    - 현재 톱니바퀴의 왼쪽 이빨, 오른쪽 이빨을 글로벌 변수로 선언해두고 추적한다.
    - 현재 톱니바퀴에서 출발하여
        - 왼쪽으로 쭉 진행하며 톱니를 돌리며, 왼쪽 이빨과 회전 방향을 갱신한다.
        - 오른쪽으로 쭉 진행하며 톱니를 돌리며, 오른쪽 이빨과 회전 방향을 갱신한다.
"""
