# 배열 돌리기 3
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cmds = list(map(int, input().split()))


# 상하 반전
# 배열 전체를 뒤집는다.
def op1(arr):
    return arr[::-1]


# 좌우 반전
# 각 행을 뒤집어서 append.
def op2(arr):
    ret = []
    row_len = len(arr)
    for i in range(row_len):
        ret.append(arr[i][::-1])
    return ret


# 오른쪽 90도 회전
# 유명한 원라이너
def op3(arr):
    return list(map(list, zip(*arr[::-1])))


# 왼쪽 90도 회전
# 방법1: 오른쪽 회전 3번
# 방법2: 각 행을 뒤집은 다음 zip 원라이너
# 방법3: 정석대로
# 내 선택: 방법1
def op4(arr):
    for _ in range(3):
        arr = op3(arr)
    return arr


# 사분면 시계방향 이동
# 주어진 그대로 구현
def op5(arr):
    row_cnt = len(arr)
    col_cnt = len(arr[0])
    row_half = row_cnt // 2
    col_half = col_cnt // 2
    ret = [[0] * col_cnt for _ in range(row_cnt)]
    for i in range(row_cnt):
        for j in range(col_cnt):
            # 그룹1
            if i < row_half and j < col_half:
                ret[i][j + col_half] = arr[i][j]
            # 그룹2
            elif i < row_half and j >= col_half:
                ret[i + row_half][j] = arr[i][j]
            # 그룹3
            elif i >= row_half and j >= col_half:
                ret[i][j - col_half] = arr[i][j]
            # 그룹4
            elif i >= row_half and j < col_half:
                ret[i - row_half][j] = arr[i][j]
    return ret


# 사분면 반시계방향 이동
# op5 약간만 변경
def op6(arr):
    row_cnt = len(arr)
    col_cnt = len(arr[0])
    row_half = row_cnt // 2
    col_half = col_cnt // 2
    ret = [[0] * col_cnt for _ in range(row_cnt)]
    for i in range(row_cnt):
        for j in range(col_cnt):
            # 그룹1
            if i < row_half and j < col_half:
                ret[i + row_half][j] = arr[i][j]
            # 그룹2
            elif i < row_half and j >= col_half:
                ret[i][j - col_half] = arr[i][j]
            # 그룹3
            elif i >= row_half and j >= col_half:
                ret[i - row_half][j] = arr[i][j]
            # 그룹4
            elif i >= row_half and j < col_half:
                ret[i][j + col_half] = arr[i][j]
    return ret


# if-else 보다 깔끔한 방법
ops = [op1, op2, op3, op4, op5, op6]
for cmd in cmds:
    arr = ops[cmd - 1](arr)

# print(end=" ") 보다 깔끔한 방법
for row in arr:
    print(*row)
