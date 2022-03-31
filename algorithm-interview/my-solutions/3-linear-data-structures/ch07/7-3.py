from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            num_to_idx[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in num_to_idx and i != num_to_idx[target - num]:
                return [i, num_to_idx[target - num]]


### Time Complexity
# for문은 1중첩 뿐이고, dict(해시테이블)의 조회는 평균 O(1) 이므로 전체는 O(n).

### Note
# 속도는 dict가 제일 빠르다는 것을 기억하자.
