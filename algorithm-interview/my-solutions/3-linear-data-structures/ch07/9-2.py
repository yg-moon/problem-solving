from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 `sum` 계산
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum = 0 인 경우이므로 정답에 추가
                    triplets.append([nums[i], nums[left], nums[right]])

                    # 중복 조합을 방지하기 위해, 바로 옆에 같은 값이 있다면 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return triplets


### Time Complexity
# for문 하나가 O(n)이고, 그 내부에서 매 번 수행되는 투포인터 풀이가 O(n).
# 따라서 전체는 O(n^2).

### Note
# 중복된 된 값을 건너뛰는 것에 주의해야 한다. (i의 방법과 j,k의 방법이 다르다)
