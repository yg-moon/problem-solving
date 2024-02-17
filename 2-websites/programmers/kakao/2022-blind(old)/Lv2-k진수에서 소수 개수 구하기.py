from math import sqrt


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def convert_base(n, k):
    result = []
    while n >= k:
        n, mod = divmod(n, k)
        result.append(str(mod))
    result.append(str(n))
    return "".join(result[::-1])


def solution(n, k):
    conv_num = convert_base(n, k)
    conv_num_splt = conv_num.split("0")

    cnt = 0
    for n in conv_num_splt:
        if n != "" and is_prime(int(n)):
            cnt += 1
    return cnt
