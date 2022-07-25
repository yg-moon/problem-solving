class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(start: int) -> str:
            # Odd length palindrome
            left = start - 1
            right = start + 1
            odd_palindrome = s[start]

            while left > -1 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            odd_palindrome = s[left+1 : right]
            
            # Even length palindrome
            right = start + 1
            even_palindrome = s[start]
            
            while start > -1 and right < len(s):
                if s[start] == s[right]:
                    start -= 1
                    right += 1
                else:
                    break
            even_palindrome = s[start+1 : right]
            
            # Return the longer
            if len(odd_palindrome) > len(even_palindrome):
                return odd_palindrome
            else:
                return even_palindrome 
        
        # Edge cases
        if len(s) == 1 or s == s[::-1]:
            return s

        # Run the helper function through the string
        longest_palindrome = ''
        current_palindrome = ''
        for i in range(len(s)):
            current_palindrome = getPalindrome(i)
            if len(longest_palindrome) < len(current_palindrome):
                longest_palindrome = current_palindrome
        
        return longest_palindrome
