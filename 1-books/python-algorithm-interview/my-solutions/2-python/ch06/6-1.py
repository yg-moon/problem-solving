class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) == 1 or s == s[::-1]:
            return s

        # 슬라이딩 윈도우 우측으로 이동
        longest_substring = ''
        for i in range(len(s) - 1):
            longest_substring = max(longest_substring,
                                expand(i, i + 1),
                                expand(i, i + 2),
                                key=len)
        return longest_substring


### Time Complexity
# for문이 O(n), expand()가 O(n)이므로 전체는 O(n^2).

### Note
# 회문의 길이가 홀수, 짝수인 경우 모두 잘 커버해야 한다.
# 문자열 전체가 회문일 경우의 예외처리만으로도 런타임이 엄청나게 단축된다.
