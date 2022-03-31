from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        # Product for numbers to the left
        product = 1
        for i in range(len(nums)):
            answer.append(product)
            product *= nums[i]

        # Multiply by product for the numbers to the right
        product = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= product
            product *= nums[i]

        return answer


### Time Complexity
# O(n)

### Note
# 원래는 배열 2개를 써야 하는데 최적화를 통해 1개로 해결한 풀이다.
