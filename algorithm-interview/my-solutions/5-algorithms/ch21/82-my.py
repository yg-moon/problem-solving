# Brute Force
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content_child = 0

        for i in range(len(s)):
            for j in range(len(g)):
                if s[i] >= g[j]:
                    content_child += 1
                    g.remove(g[j])
                    break

        return content_child
