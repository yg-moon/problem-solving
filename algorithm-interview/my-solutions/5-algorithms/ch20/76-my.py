# Time Limit Exceeded at 265/266 test case.
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 예외처리
        if len(s) < len(t):
            return ""

        def isSubstring(s: str) -> bool:
            s_cnt = collections.Counter(s)
            for c in t:
                if c not in s_cnt or s_cnt[c] == 0:
                    return False
                else:
                    s_cnt[c] -= 1
            return True

        for window_len in range(len(t), len(s) + 1):
            for i in range(len(s) - window_len + 1):
                window = s[i : i + window_len]
                if isSubstring(window):
                    return "".join(window)

        return ""
