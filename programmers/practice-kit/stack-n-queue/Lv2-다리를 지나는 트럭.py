from collections import deque


def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)  # 대기중인 트럭들
    bridge = deque()  # 현재 다리 상황 [(트럭 무게1, 들어온 시각1),...]
    done = []  # 다리를 지난 트럭들
    cur_bridge_weight = 0
    cur_time = 0

    while len(done) != len(truck_weights):
        cur_time += 1

        # bridge -> done 으로 트럭 이동
        if bridge:
            truck_weight, in_time = bridge[0]
            # 현재 시각 - 들어온 시각 = 다리 길이이면 다리를 지나감
            if cur_time - in_time == bridge_length:
                done.append(bridge.popleft())
                cur_bridge_weight -= truck_weight

        # trucks -> bridge 으로 트럭 이동
        if trucks and cur_bridge_weight + trucks[0] <= weight:
            truck_weight = trucks.popleft()
            bridge.append((truck_weight, cur_time))
            cur_bridge_weight += truck_weight

    return cur_time
