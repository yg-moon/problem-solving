from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binarySearch(nums: List, target: int):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return -1

        # 짧은게 nums1이 되도록
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2
        nums2.sort()

        answer = []
        for num in nums1:
            result = binarySearch(nums2, num)
            if result != -1 and num not in answer:
                answer.append(num)

        return answer
