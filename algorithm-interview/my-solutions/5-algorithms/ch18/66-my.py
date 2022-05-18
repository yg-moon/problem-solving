# 어디서 꺾였는지 알면, 그 기준으로 2개 배열로 구분해서 각각 이진탐색.
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 예외 처리
        if not nums:
            return -1

        # 최소값 찾아 피벗 설정
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        # 이진 탐색
        def binarySearch(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        # 두 배열에 각각 이진 탐색
        result_1 = binarySearch(pivot, len(nums) - 1)
        result_2 = binarySearch(0, pivot - 1)
        if result_1 != -1:
            return result_1
        elif result_2 != -1:
            return result_2
        else:
            return -1
