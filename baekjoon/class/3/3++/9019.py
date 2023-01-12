# DSLR
from collections import deque

ops = ["D", "S", "L", "R"]


def trans(n, op):
    ret = -1
    if op == "D":
        ret = (2 * n) % 10000
    elif op == "S":
        ret = n - 1
        if ret == -1:
            ret = 9999
    else:
        str_n = str(n)
        if len(str_n) < 4:
            str_n = "0" * (4 - len(str_n)) + str_n
        if op == "L":
            ret = int(str_n[1:] + str_n[0])
        if op == "R":
            ret = int(str_n[-1] + str_n[:-1])
    return ret


T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    # BFS
    q = deque([[A, ""]])
    visited = set()
    while q:
        num, cmd = q.popleft()
        if num == B:
            print(cmd)
            break
        for op in ops:
            next = trans(num, op)
            if next not in visited:
                visited.add(next)
                q.append([next, cmd + op])

"""
- 난이도: 골드4
- 분류: BFS

핵심
- BFS라는걸 알아채는게 중요한 문제.
- 최단경로와 비슷한 개념이 나오면 떠올리자.

디버깅
- 상황: '틀렸습니다'
- 원인: 4자리 이하 숫자는 비어있는 왼쪽 칸을 0으로 채워야 한다.
    - ex. 123을 L연산 수행시 231이 아니라, 1230이 되어야 함. (0123 이기 때문)
    - ex. 123을 R연산 수행시 312가 아니라 3012가 되어야 함. (0123 이기 때문)
"""
