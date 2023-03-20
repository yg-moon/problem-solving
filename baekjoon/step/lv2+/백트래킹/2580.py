# 스도쿠
arr = [list(map(int, input().split())) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zeros.append((i, j))


def is_ok(x, y, n):
    # 현재 행에 같은 숫자가 있는지 확인
    for j in range(9):
        if arr[x][j] == n:
            return False
    # 현재 열에 같은 숫자가 있는지 확인
    for i in range(9):
        if arr[i][y] == n:
            return False
    # 현재 3x3 사각형에 같은 숫자가 있는지 확인
    base_x = x // 3 * 3
    base_y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if arr[base_x + i][base_y + j] == n:
                return False
    return True


def solve(cnt):
    if cnt == len(zeros):
        for a in arr:
            print(*a)
        exit(0)
    else:
        cur_x = zeros[cnt][0]
        cur_y = zeros[cnt][1]
        for num in range(1, 10):
            if is_ok(cur_x, cur_y, num):
                arr[cur_x][cur_y] = num
                solve(cnt + 1)
                arr[cur_x][cur_y] = 0


solve(0)

"""
- 난이도: 골드4
- 분류: 백트래킹

배운점
- 3x3 사각형을 확인할때, 같은 로직이지만 더 간단하게 쓸 수 있다.
- 원리: 0~9 범위의 수를 3으로 나눈 몫에 다시 3을 곱하면, [0, 3, 6] 중 하나에 속하게 된다.
"""
