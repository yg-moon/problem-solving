class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = 0
        start = 0
        for i, char in enumerate(s):
            # If char in seen within the window range, update start.
            if char in seen and start <= seen[char]:
                start = seen[char] + 1
            else:
                max_length = max(max_length, i - start + 1)

            # Save recent index for this char
            seen[char] = i

        return max_length
