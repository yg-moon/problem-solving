# Recursive
def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)


# Top-Down DP
dp_td = [-1] * 50


def fib2(n):
    if dp_td[n] == -1:
        if n == 0:
            dp_td[n] = 0
        elif n == 1:
            dp_td[n] = 1
        else:
            dp_td[n] = fib2(n - 1) + fib2(n - 2)
    return dp_td[n]


# Bottom-Up DP
dp_bu = [0] * 50


def fib3(n):
    dp_bu[n] = 0
    dp_bu[1] = 1
    for i in range(2, n + 1):
        dp_bu[i] = dp_bu[i - 1] + dp_bu[i - 2]
    return dp_bu[n]
