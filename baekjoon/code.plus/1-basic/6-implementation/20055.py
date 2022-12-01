# 컨베이어 벨트 위의 로봇
N, K = map(int, input().split())
belt = list(map(int, input().split()))
robots = [0] * (2 * N)
robot_num = 1
steps = 0


def rotate(arr, type):
    ret = [0] * (2 * N)
    for i in range(2 * N):
        ret[(i + 1) % (2 * N)] = arr[i]
    # 내리는 위치에 있는 로봇은 내리기
    if type == "robots" and ret[N - 1] != 0:
        ret[N - 1] = 0
    return ret


def move_robots():
    for num in sorted(robots):
        idx = robots.index(num)
        if num != 0 and robots[idx + 1] == 0 and belt[idx + 1] >= 1:
            robots[idx + 1] = num
            robots[idx] = 0
            belt[idx + 1] -= 1
            # 내리는 위치에 있는 로봇은 내리기
            if robots[N - 1] != 0:
                robots[N - 1] = 0


def simulate():
    global belt, robots, robot_num, steps
    while True:
        # 1.
        belt = rotate(belt, "belt")
        robots = rotate(robots, "robots")
        # 2.
        move_robots()
        # 3.
        if belt[0] != 0:
            robots[0] = robot_num
            robot_num += 1
            belt[0] -= 1
        # 4.
        steps += 1
        if belt.count(0) >= K:
            return


simulate()
print(steps)

"""
- 요약: 주어진 그대로 구현
- 구현
    - 벨트와 로봇을 회전하는 방법
        - % 연산자
    - 가장 먼저 올라간 로봇부터 이동하는 방법
        - 각 로봇에 고유번호를 부여하고, 현재 로봇배열을 정렬해서 가장 작은 번호의 로봇부터 이동.
    - 핵심 요구사항
        - 내리는 위치 (N-1번째 인덱스)에 도달한 로봇은 즉시 내리기
        - 로봇이 올라가거나 이동하는 순간 벨트의 내구도 깎기
"""
