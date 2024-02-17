from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        answer.append(max(nums[:k]))

        i = 1
        j = k

        while j < len(nums):
            # 최댓값이 변경될 경우에만 재계산
            if nums[j] > answer[-1]:
                answer.append(nums[j])
            elif nums[i - 1] == answer[-1]:
                answer.append(max(nums[i : j + 1]))
            else:
                answer.append(answer[-1])
            i += 1
            j += 1

        return answer


# TLE
