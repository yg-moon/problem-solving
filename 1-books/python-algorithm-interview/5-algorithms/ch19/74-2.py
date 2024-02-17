class Solution:
    def hammingWeight(self, n: int) -> int:
        # 자신에서 매번 1을 뺀 값과 AND 연산 횟수 측정
        cnt = 0
        while n:
            n &= n - 1
            cnt += 1
        return cnt
