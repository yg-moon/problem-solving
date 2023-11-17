from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def shift_row(mat):
    deq_mat = deque(mat)
    tmp = deq_mat.pop()
    deq_mat.appendleft(tmp)
    return list(deq_mat)


def rotate(mat):
    dir = 0
    x = 0
    y = 0
    val = mat[x][y]
    n = len(mat)
    m = len(mat[0])

    while dir < 4:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < m:
            tmp = mat[nx][ny]
            mat[nx][ny] = val
            val = tmp
            x = nx
            y = ny
        else:
            dir += 1

    return mat


def solution(rc, operations):
    for op in operations:
        if op == "ShiftRow":
            rc = shift_row(rc)
        elif op == "Rotate":
            rc = rotate(rc)

    return rc


"""
- 단순 구현 풀이 (정확성 100점, 효율성 시간초과)
- 소요 시간: 9:05-9:25 (20분) 
"""
