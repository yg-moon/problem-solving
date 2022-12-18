from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 피벗(최솟값)의 인덱스 찾기
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        # 기본 이진 검색
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

        # 두 배열에 각각 이진 검색
        result_1 = binarySearch(0, pivot - 1)
        result_2 = binarySearch(pivot, len(nums) - 1)
        if result_1 != -1:
            return result_1
        elif result_2 != -1:
            return result_2
        else:
            return -1


"""
- 어디서 꺾였는지 알면, 그 기준으로 2개의 배열로 구분해서 각각 이진 검색. 
"""
