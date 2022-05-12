from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 주유소 기름 총합 < 이동 비용 총합 이라면 가능한 경로가 없다.
        if sum(gas) < sum(cost):
            return -1

        # 가능한 경로가 반드시 있다는 가정하에서 탐색
        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안되는 지점 판별
            if gas[i] + fuel < cost[i]:
                # 안되는 지점이 있다면 그 이후부터 다시 탐색.
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start
