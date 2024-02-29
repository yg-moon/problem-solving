class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        # 예외처리
        if len(A) != len(B):
            return False
        if A == B:
            return True

        # 핵심: 이어 붙인 것 안에 있는지
        if B in A + A:
            return True
        else:
            return False


"""
- 난이도: Easy
- 분류: 문자열
"""
