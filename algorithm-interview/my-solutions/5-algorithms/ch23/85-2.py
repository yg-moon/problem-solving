import collections


class Solution:
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        # 핵심1: 값이 존재하면 그대로 리턴
        if self.dp[N]:
            return self.dp[N]

        # 핵심2: 반복문 없음! (이 문제만)
        self.dp[N] = self.fib(N - 1) + self.fib(N - 2)

        return self.dp[N]
