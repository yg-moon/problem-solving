from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binarySearch(nums: List, target: int):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return -1

        # 이진 검색할 배열은 정렬
        nums2.sort()

        answer = []
        for num in nums1:
            result = binarySearch(nums2, num)
            if result != -1 and num not in answer:
                answer.append(num)
        return answer
