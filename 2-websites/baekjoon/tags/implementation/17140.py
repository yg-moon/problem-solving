# 이차원 배열과 연산
from collections import defaultdict

R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

len_r = 3
len_c = 3
answer = 0


def rotate_right(mat):
    return [list(row) for row in zip(*mat[::-1])]


def rotate_left(mat):
    return [list(row) for row in zip(*mat)][::-1]


def op_r():
    global arr, len_c

    ret = []
    max_len = 0

    # 각 행을 정렬
    for row in arr:
        new_row = []
        dic = defaultdict(int)
        for x in row:
            if x != 0:  # 0은 제외
                dic[x] += 1
        items = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        for num, cnt in items:
            new_row.extend([num, cnt])
        ret.append(new_row)
        max_len = max(max_len, len(items) * 2)

    # 0 맞추기
    for row in ret:
        diff = max_len - len(row)
        if diff > 0:
            row.extend([0] * diff)

    arr = ret
    len_c = max_len


def op_c():
    global arr, len_r

    ret = []
    ret2 = []
    max_len = 0

    # 오른쪽으로 회전 (행단위로 작업하기 위해)
    arr = rotate_right(arr)

    # 각 행을 정렬
    for row in arr:
        new_row = []
        dic = defaultdict(int)
        for x in row:
            if x != 0:  # 0은 제외
                dic[x] += 1
        items = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        for num, cnt in items:
            new_row.extend([num, cnt])
        ret.append(new_row)
        max_len = max(max_len, len(items) * 2)

    # 0 맞추기
    for row in ret:
        diff = max_len - len(row)
        if diff > 0:
            row.extend([0] * diff)

    # 다시 열 기준으로 맞추기: 각 행을 뒤집고, 전체 왼쪽 회전
    for row in ret:
        ret2.append(row[::-1])
    ret2 = rotate_left(ret2)

    arr = ret2
    len_r = max_len


while answer <= 100:
    # 주의: 인덱스 범위 확인
    if len_r >= R and len_c >= C and arr[R - 1][C - 1] == K:
        break
    if len_r >= len_c:
        op_r()
    else:
        op_c()
    answer += 1

if answer <= 100:
    print(answer)
else:
    print(-1)

"""
- 난이도: 골드4
- 분류: 시뮬레이션
- 소요 시간: 50분

핵심
- 행 연산: 시키는대로 하면 됨
- 열 연산: 회전 시켜서 행 단위로 작업하고, 다시 회전

조건 정리
- 기준: 등장 횟수 오름차순, 수 오름차순
- 결과: (수, 등장 횟수)
"""
