def solution(cap, n, deliveries, pickups):
    # d_i, p_i: 배달 및 수거를 해야하는 마지막 집을 가리키는 인덱스
    d_i = n - 1
    p_i = n - 1
    answer = 0

    # 초기화
    while deliveries[d_i] == 0 and d_i >= 0:
        d_i -= 1
    while pickups[p_i] == 0 and p_i >= 0:
        p_i -= 1

    # 핵심: 매번 가장 먼 집까지 배달 및 수거
    while d_i >= 0 or p_i >= 0:  # 주의: and가 아니라 or로 써야함!
        # 정답거리 추가
        if d_i >= p_i:
            answer += 2 * (d_i + 1)
        else:
            answer += 2 * (p_i + 1)

        # 마지막 집부터 배달
        cur_cap = cap
        while cur_cap > 0 and d_i >= 0:
            if deliveries[d_i] <= cur_cap:
                cur_cap -= deliveries[d_i]
                deliveries[d_i] = 0
                d_i -= 1
            else:
                deliveries[d_i] -= cur_cap
                cur_cap = 0
        # 당겨주기
        while deliveries[d_i] == 0 and d_i >= 0:
            d_i -= 1

        # 마지막 집부터 수거
        cur_cap = cap
        while cur_cap > 0 and p_i >= 0:
            if pickups[p_i] <= cur_cap:
                cur_cap -= pickups[p_i]
                pickups[p_i] = 0
                p_i -= 1
            else:
                pickups[p_i] -= cur_cap
                cur_cap = 0
        # 당겨주기
        while pickups[p_i] == 0 and p_i >= 0:
            p_i -= 1

    return answer


"""
- 분류: 그리디
- 소요 시간: 2:00-2:50 (50분)

요약
- 가면서 뿌릴 수 있고, 오면서 수거할 수 있음
- 매번 가장 먼곳까지 배달 및 수거

디버깅
- 상황: 답이 틀림
- 해결: 조건문에서 and를 or로 바꾸니 성공!
"""
