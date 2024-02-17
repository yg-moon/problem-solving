# 배열 돌리기 6
N, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
ops = [list(map(int, input().split())) for _ in range(R)]


# 부분배열 내부를 상하 반전
def op1(arr, l):
    ret = [[0] * 2**N for _ in range(2**N)]
    for i in range(0, 2**N, 2**l):
        for j in range(0, 2**N, 2**l):
            for cur_i in range(i, i + 2**l):
                for cur_j in range(j, j + 2**l):
                    ret[i + 2**l - 1 - (cur_i - i)][cur_j] = arr[cur_i][cur_j]
    return ret


# 부분배열 내부를 좌우 반전
def op2(arr, l):
    ret = [[0] * 2**N for _ in range(2**N)]
    for i in range(0, 2**N, 2**l):
        for j in range(0, 2**N, 2**l):
            for cur_i in range(i, i + 2**l):
                for cur_j in range(j, j + 2**l):
                    ret[cur_i][j + 2**l - 1 - (cur_j - j)] = arr[cur_i][cur_j]
    return ret


# 부분배열 내부를 90도 우회전
def op3(arr, l):
    ret = [[0] * 2**N for _ in range(2**N)]
    for i in range(0, 2**N, 2**l):
        for j in range(0, 2**N, 2**l):
            for cur_i in range(i, i + 2**l):
                for cur_j in range(j, j + 2**l):
                    ret[i + (cur_j - j)][j + 2**l - 1 - (cur_i - i)] = arr[cur_i][
                        cur_j
                    ]
    return ret


# 부분배열 내부를 90도 좌회전
def op4(arr, l):
    ret = [[0] * 2**N for _ in range(2**N)]
    for i in range(0, 2**N, 2**l):
        for j in range(0, 2**N, 2**l):
            for cur_i in range(i, i + 2**l):
                for cur_j in range(j, j + 2**l):
                    ret[i + 2**l - 1 - (cur_j - j)][j + (cur_i - i)] = arr[cur_i][
                        cur_j
                    ]
    return ret


# 부분배열을 단위로 상하반전
def op5(arr, l):
    ret = [[0] * 2**N for _ in range(2**N)]
    for i in range(0, 2**N, 2**l):
        for j in range(0, 2**N, 2**l):
            new_i = 2**N - 1 - i - (2**l - 1)
            for cur_i in range(i, i + 2**l):
                for cur_j in range(j, j + 2**l):
                    ret[new_i + (cur_i - i)][cur_j] = arr[cur_i][cur_j]
    return ret


# 부분배열을 단위로 좌우반전
def op6(arr, l):
    ret = [[0] * 2**N for _ in range(2**N)]
    for i in range(0, 2**N, 2**l):
        for j in range(0, 2**N, 2**l):
            new_j = 2**N - 1 - j - (2**l - 1)
            for cur_i in range(i, i + 2**l):
                for cur_j in range(j, j + 2**l):
                    ret[cur_i][new_j + (cur_j - j)] = arr[cur_i][cur_j]
    return ret


# 부분배열을 단위로 90도 우회전
def op7(arr, l):
    ret = [[0] * 2**N for _ in range(2**N)]
    for i in range(0, 2**N, 2**l):
        for j in range(0, 2**N, 2**l):
            new_i = j
            new_j = 2**N - 1 - i - (2**l - 1)
            for cur_i in range(i, i + 2**l):
                for cur_j in range(j, j + 2**l):
                    ret[new_i + (cur_i - i)][new_j + (cur_j - j)] = arr[cur_i][cur_j]
    return ret


# 부분배열을 단위로 90도 좌회전
def op8(arr, l):
    ret = [[0] * 2**N for _ in range(2**N)]
    for i in range(0, 2**N, 2**l):
        for j in range(0, 2**N, 2**l):
            new_i = 2**N - 1 - j - (2**l - 1)
            new_j = i
            for cur_i in range(i, i + 2**l):
                for cur_j in range(j, j + 2**l):
                    ret[new_i + (cur_i - i)][new_j + (cur_j - j)] = arr[cur_i][cur_j]
    return ret


funcs = [0, op1, op2, op3, op4, op5, op6, op7, op8]

for k, l in ops:
    arr = funcs[k](arr, l)

for row in arr:
    print(*row)

"""
- 요약: 주어진 그대로 구현
- 구현
    - 부분배열 내부 변경 (op1~4)
        - cur_i가 0부터 시작하는게 아니므로, cur_i - i를 통해 상대위치로 표현해야 한다.
        - 각 부분배열에서 위치를 보정하려면 현재 시작점인 i또는 j를 기준으로 출발해야 한다.
    - 부분배열 단위 변경 (op5~8)
        - 부분배열의 좌상단을 기준으로 변경된 위치를 파악하여, 그곳에서부터 뿌려준다.
"""
