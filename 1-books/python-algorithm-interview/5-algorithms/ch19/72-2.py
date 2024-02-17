class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        # 합, 자릿수 처리
        # a: carry 값을 고려하지 않는 a와 b의 합 (sum).
        # b: 자릿수를 올려가며 carry 값을 담음.
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # 음수 처리
        if a > INT_MAX:
            a = ~(a ^ MASK)

        return a
