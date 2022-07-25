from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


### Time Complexity
# 리스트 길이의 절반(1/2 * n)만큼 스왑이 이루어지므로 O(n).

### Note
# 문자열 길이가 홀수, 짝수일 때 모두 잘 동작해야 한다.
