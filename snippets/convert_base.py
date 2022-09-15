# 숫자 n을 k진수로 변환한 결과
def convert_base(n, k):
    result = []
    while n >= k:
        n, mod = divmod(n, k)
        result.append(str(mod))
    result.append(str(n))
    return "".join(result[::-1])
