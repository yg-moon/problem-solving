# Wrong Answer

import sys


def solution(queue1, queue2):
    min_op = sys.maxsize
    target = (sum(queue1) + sum(queue2)) // 2
    seen = []

    def check(op, q1):
        if sum(q1) == target:
            nonlocal min_op
            min_op = min(min_op, op)

    def run(queue1, queue2):
        for i in range(len(queue1)):
            op = 0
            q1 = queue1[:]
            q2 = queue2[:]
            for _ in range(i):
                if q1:
                    q2.append(q1.pop(0))
                    op += 1
            for j in range(len(q2)):
                for _ in range(j):
                    if q2:
                        q1.append(q2.pop(0))
                        op += 1
                    # print("op", op)
                    # print("q1", q1)
                    # print("q2", q2)
                    # print("")
                    if q1 not in seen:
                        seen.append(q1[:])
                    if q2 not in seen:
                        seen.append(q2[:])
                    
                    # 이렇게 해야 최적화 될거 같은데 결과가 틀림
                    # if q1 not in seen and q2 not in seen:
                    #     check(op, q1)
                    # 사실 애초에 중복조합 나오지 않게 pop, append 해야 하는건가? (가능한가?)
                    check(op, q1)
    
    run(queue1, queue2)
    run(queue2, queue1)

    if min_op == sys.maxsize:
        min_op = -1

    return min_op


# 최적화
# 매번 두큐의 합이 같은지 확인하지 말고, 처음에 총합/2 를 목표로 잡고 한 큐만 검사.
# seen에 넣어서 이미 봤던 조합은 검사하지 않도록.
# deque로 popleft 최적화 가능.