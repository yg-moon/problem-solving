from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        
        # 더 높은 쪽을 향해 투 포인터 이동
        while left < right:
            if left_max <= right_max:
                water += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                water += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])

        return water


### Time Complexity
# 전체 배열을 한번만 훑으므로 O(n).

### Note
# 더 높은 쪽을 향해 투 포인터를 이동해야 오류가 없음을 보장할 수 있다.
# 그렇지 않으면 반대쪽 벽이 막혀 있지 않을 가능성 때문에 물을 잘못 더하게 된다.
