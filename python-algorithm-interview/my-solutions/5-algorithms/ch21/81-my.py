# Time Limit Exceeded
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        can_complete = False
        ans_idx = -1

        for i in range(len(gas)):
            if can_complete:
                break

            travel_cnt = 0
            can_travel = True
            tank = 0
            curr_idx = i
            while travel_cnt < len(gas) and can_travel:
                if curr_idx == len(gas) - 1:
                    next_idx = 0
                else:
                    next_idx = curr_idx + 1

                if tank + gas[curr_idx] >= cost[curr_idx]:
                    tank += gas[curr_idx] - cost[curr_idx]
                    travel_cnt += 1
                    curr_idx = next_idx
                else:
                    can_travel = False
            
            if can_travel:
                ans_idx = i

        return ans_idx
