from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    l_sum = sum(q1)
    r_sum = sum(q2)
    max_cnt = 3 * len(queue1)
    answer = 0

    # 큐 길이의 3배까지
    while answer < max_cnt:
        # q1의 원소를 q2로 넘긴다
        if l_sum > r_sum:
            tmp = q1.popleft()
            q2.append(tmp)
            l_sum -= tmp
            r_sum += tmp
        # q2의 원소를 q1으로 넘긴다
        elif l_sum < r_sum:
            tmp = q2.popleft()
            q1.append(tmp)
            r_sum -= tmp
            l_sum += tmp
        else:
            return answer
        answer += 1

    return -1


"""
- 분류: 그리디 (정해)
- 소요 시간: 2:15-2:30 (15분)
"""
