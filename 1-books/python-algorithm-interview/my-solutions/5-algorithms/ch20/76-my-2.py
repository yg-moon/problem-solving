from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ctr_t = Counter(t)

        for length in range(len(t), len(s) + 1):
            for start in range(len(s)):
                if start + length <= len(s):
                    substr = s[start : start + length]
                    if Counter(substr) >= ctr_t:
                        return substr

        return ""


# TLE
