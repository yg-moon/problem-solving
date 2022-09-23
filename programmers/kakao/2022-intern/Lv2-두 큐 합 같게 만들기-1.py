# 그리디 풀이
from collections import deque


def solution(queue1, queue2):
    L = sum(queue1)
    R = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    max_cnt = len(queue1) * 3
    answer = 0

    while answer < max_cnt:
        # L > R이라면, q1의 원소를 q2로 넘긴다.
        if L > R:
            tmp = q1.popleft()
            q2.append(tmp)
            L -= tmp
            R += tmp
        # L < R이라면, q2의 원소를 q1로 넘긴다.
        elif L < R:
            tmp = q2.popleft()
            q1.append(tmp)
            L += tmp
            R -= tmp
        else:
            return answer
        answer += 1

    return -1
