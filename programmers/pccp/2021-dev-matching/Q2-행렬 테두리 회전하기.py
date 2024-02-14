# 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def rotate(mat, x1, y1, x2, y2):
    d = 0  # 방향
    x = x1
    y = y1
    min_num = mat[x][y]
    prev = mat[x][y]

    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        # 범위를 벗어났다면 방향전환
        if not (x1 <= nx <= x2 and y1 <= ny <= y2):
            if d == 3:
                break
            else:
                d += 1
        # 한칸씩 밀어내기
        else:
            cur = mat[nx][ny]
            min_num = min(min_num, cur)
            mat[nx][ny] = prev
            prev = cur
            x = nx
            y = ny

    return [mat, min_num]


def solution(rows, columns, queries):
    # N*M 행렬 만들기
    N = rows
    M = columns
    mat = [[0] * columns for _ in range(rows)]
    num = 1
    for i in range(N):
        for j in range(M):
            mat[i][j] = num
            num += 1

    # 배열 회전하고 최솟값 구하기
    answer = []
    for x1, y1, x2, y2 in queries:
        mat, min_num = rotate(mat, x1 - 1, y1 - 1, x2 - 1, y2 - 1)
        answer.append(min_num)
    return answer


"""
- 난이도: Lv2
- 분류: 구현
- 소요시간: 25분

요약
- 직접 행렬을 만들고, 시키는대로 회전

효율성 계산
- 100x100 행렬의 테두리의 길이는 최대 400
- 400x1만 쿼리 = 400만번 이동 -> 가능
"""
