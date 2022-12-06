from collections import deque


def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)  # 대기중인 트럭들
    bridge = deque()  # 현재 다리 상황 [(트럭 무게1, 들어온 시각1),...]
    done = []  # 다리를 지난 트럭들
    cur_total_weight = 0
    time = 0

    while len(done) != len(truck_weights):
        time += 1

        # bridge -> done 트럭 이동
        if bridge:
            truck_weight, in_time = bridge[0]
            # 현재 시각 - 들어온 시각 = 다리 길이이면 다리를 지나감
            if time - in_time == bridge_length:
                done.append(bridge.popleft())
                cur_total_weight -= truck_weight

        # trucks -> bridge 트럭 이동
        if trucks and cur_total_weight + trucks[0] <= weight:
            truck_weight = trucks.popleft()
            bridge.append((truck_weight, time))
            cur_total_weight += truck_weight

    return time


"""
- 요약: 시뮬레이션
- 구현
    - 매초마다 문제 조건대로 시뮬레이션
    - 종료 조건: 다 건넌 트럭 수와 처음 트럭 수가 같을 때
    - 다리 지나갈 조건: 현재 시각 - 들어온 시각 = 다리 길이 일 때
    - 팁: 현재 무게를 매번 sum()으로 계산하지 말고, 변수로 두고 관리하면 효율적.
- 주의
    - 1초에 한 트럭씩만 다리에 올라가고 내려갈 수 있다. (따라서 while문이 아니라 if문으로 이동)
    - deque mutated during iteration: 순회 도중에 remove() 하는 경우, 복사본 사용 필요.
"""
