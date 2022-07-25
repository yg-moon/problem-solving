# 986 / 987 test cases passed.
# Time Limit Exceeded in case 987.
# O(n^2).

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def sublen(start: int) -> int:
            end = start + 1
            if s[start] == s[end]:
                return 1

            char_to_count = defaultdict(int)
            char_to_count[s[start]] += 1
            repeating = False

            while end < len(s) and not repeating:
                char_to_count[s[end]] += 1
                for char in char_to_count:
                    if char_to_count[char] > 1:
                        end -= 1
                        repeating = True
                        break
                end += 1

            return end - start

        # Edge case
        if len(s) == 0 or len(s) == 1:
            return len(s)

        max_length = 1
        for i in range(len(s) - 1):
            max_length = max(max_length, sublen(i))
        return max_length
