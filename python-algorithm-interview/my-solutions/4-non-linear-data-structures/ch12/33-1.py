# LeetCode 17
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 예외 처리
        if not digits:
            return []

        result = []
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(idx, path):
            # 현재 조합이 길이를 만족하면 정답에 추가
            if len(path) == len(digits):
                result.append(path)
                return
            # 입력값 자릿수 단위
            for i in range(idx, len(digits)):
                # 숫자에 매핑된 문자 단위
                for j in digit_to_letters[digits[i]]:
                    dfs(i + 1, path + j)

        dfs(0, "")
        return result
