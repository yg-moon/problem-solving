from collections import deque


def solution(menu, order, k):
    q = deque()
    q.append((0, menu[order[0]]))  # (들어온 시간, 걸리는 시간)
    cur_time = 0
    last_time = 0  # 마지막 음료 제조를 완료한 시간
    max_cnt = 1

    for i in range(1, len(order)):
        # 현재시간 증가
        cur_time += k

        # 주의: (마지막 제조 완료시간 < 들어온 시간)이면, 들어온 이후부터 만들 수 있음
        if last_time < q[0][0]:
            last_time = q[0][0]

        # 나갈 사람 나가기
        while q and last_time + q[0][1] <= cur_time:
            last_time += q[0][1]
            q.popleft()

        # 다음 사람 들어오기
        q.append((cur_time, menu[order[i]]))

        # 최대 대기열 계산
        max_cnt = max(max_cnt, len(q))

    return max_cnt


"""
- 분류: 시뮬레이션, 큐
- 시간: 10:50-11:40 (50분)

- 주의: 한번에 하나의 음료만 만들 수 있음
"""
