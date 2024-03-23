# Recursive
def fib_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


# Top-Down DP
dp = [-1] * 50


def fib_td(n):
    if dp[n] != -1:
        return dp[n]

    if n <= 1:
        dp[n] = n
    else:
        dp[n] = fib_td(n - 1) + fib_td(n - 2)


# Bottom-Up DP
def fib_bu(n):
    dp = [0] * 50

    # 초기화
    dp[1] = 1

    # 점화식
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
