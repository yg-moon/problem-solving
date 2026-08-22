class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


"""
- 난이도: Easy
- 분류: 정렬, 해시
"""
