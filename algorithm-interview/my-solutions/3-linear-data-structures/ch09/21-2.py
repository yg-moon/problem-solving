from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_to_count = defaultdict(int)
        seen = set()
        stack = []

        # Fill counter info.
        for char in s:
            char_to_count[char] += 1

        # Fill stack and pop duplicate letters.
        for char in s:
            char_to_count[char] -= 1
            
            if char in seen:
                continue
            
            while stack and char < stack[-1] and char_to_count[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            seen.add(char)
            stack.append(char)

        return ''.join(stack)
