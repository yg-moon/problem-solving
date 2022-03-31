class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []

        # 대문자는 소문자로 변환, 영어/숫자 아닌건 삭제
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        return strs == strs[::-1]


# 참고: 책의 1번, 3번 풀이를 섞어서 my라고는 했지만 딱히 새로운 풀이는 없음.

# 동작 확인
# print(Solution().isPalindrome("abcba"))
# print(Solution().isPalindrome("notPalindrome"))

### Time Complexity
# for문 하나 뿐이니까 O(n).

### Note
# 인풋 길이가 최소 1로 주어지므로 고려해야 할 Edge Case는 딱히 없음.
