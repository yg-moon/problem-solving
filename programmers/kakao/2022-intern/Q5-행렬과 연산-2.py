from collections import deque


def solution(rc, operations):
    r = len(rc)
    c = len(rc[0])
    col1 = deque(rc[i][0] for i in range(r))
    col2 = deque(rc[i][-1] for i in range(r))
    rows = [deque(rc[i][j] for j in range(1, c - 1)) for i in range(r)]
    idx = 0

    for op in operations:
        if op == "ShiftRow":
            col1.appendleft(col1.pop())
            col2.appendleft(col2.pop())
            idx -= 1
            if idx == -1:
                idx = r - 1
        elif op == "Rotate":
            rows[idx].appendleft(col1.popleft())
            col2.appendleft(rows[idx].pop())
            rows[(idx - 1) % r].append(col2.pop())
            col1.append(rows[(idx - 1) % r].popleft())

    ret = [[0] * c for _ in range(r)]
    for i in range(r):
        ret[i][0] = col1.popleft()
        for j in range(1, c - 1):
            ret[i][j] = rows[(i + idx) % r].popleft()
        ret[i][c - 1] = col2.popleft()
    return ret


"""
- 자료구조(데크) 풀이
- 출처: 공식 해설, https://blog.encrypted.gg/1079
"""
