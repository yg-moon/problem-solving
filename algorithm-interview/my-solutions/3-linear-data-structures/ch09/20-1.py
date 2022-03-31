class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        
        for char in s:
            # If left bracket, push to stack.
            if char not in table:
                stack.append(char)
            # If right bracket, pop from stack and check if pair matches.
            else:
                # Also, if stack is already empty, not valid.
                if not stack or table[char] != stack.pop():
                    return False
        
        # If unmatched left brackets exist, not valid.
        if stack:
            return False

        return True
