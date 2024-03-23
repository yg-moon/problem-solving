# 숫자 n을 k진수로 변환한 결과
def convert_base(n, k):
    lst = []
    while n >= k:
        div, mod = divmod(n, k)
        lst.append(mod)
        n = div
    lst.append(n)
    return "".join(str(x) for x in reversed(lst))


# Test
print(convert_base(8, 2))
