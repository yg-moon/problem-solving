# 정육면체 전개도
figures = [[list(map(int, input().split())) for _ in range(6)] for _ in range(3)]
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # L R U D
patterns = [
    [3, 1, 2],
    [3, 3, 0, 0],
    [3, 1, 1, 2],
    [3, 3, 3, 3],
    [3, 1, 1, 1, 2],
    [3, 3, 3, 0, 3],
]  # 허용되지 않는 패턴 목록 (방향 기준)


def rotate(board):
    return list(map(list, zip(*board[::-1])))


# 현재 좌표를 기준으로 검사
def check_point(x, y, figure):
    for pattern in patterns:
        cur_x = x
        cur_y = y
        found = True
        for p in pattern:
            nx = cur_x + dirs[p][0]
            ny = cur_y + dirs[p][1]
            if 0 <= nx < 6 and 0 <= ny < 6:
                if figure[nx][ny] == 1:
                    cur_x = nx
                    cur_y = ny
                # 찾는 중에 끊어지면 다음 패턴으로 넘어감
                else:
                    found = False
                    break
            # 범위를 벗어날 경우 다음 패턴으로 넘어감
            else:
                found = False
                break
        # 허용되지 않는 패턴이 전개도에 하나라도 존재할 경우
        if found:
            return False
    return True


# 하나의 전개도에 대해 확인
def check_figure(figure):
    for i in range(6):
        for j in range(6):
            if figure[i][j] == 1:
                if not check_point(i, j, figure):
                    return False
    return True


# 모든 전개도를 4방향으로 돌려가면서 확인
for figure in figures:
    is_possible = True
    for _ in range(4):
        figure = rotate(figure)
        if not check_figure(figure):
            is_possible = False
    if is_possible:
        print("yes")
    else:
        print("no")

"""
- 요약: 허용되지 않는 모든 패턴을 찾고, 각 전개도에 그런 패턴이 하나라도 있는지 확인.
- 구현
    - 허용되지 않는 패턴은 총 6개.
    - 찾은 방법
        - 핵심: 어떤 전개도가 정육면체를 만들 수 있는(or 없는) 조건은 무엇인가?
        - 시도: 전개도에서 가능한 위치, 불가능한 위치를 표시해보며 패턴 파악.
    - 배열을 4번 돌리면서 모든 위치에 상대좌표로 확인.
"""
