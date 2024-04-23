def convert_base(n, k):
    lst = []
    while n >= k:
        div, mod = divmod(n, k)
        lst.append(mod)
        n = div
    lst.append(n)
    return "".join(str(x) for x in reversed(lst))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    converted = convert_base(n, k)
    answer = 0
    for num in converted.split("0"):
        if num != "" and is_prime(int(num)):  # 주의: 빈 문자열 예외처리
            answer += 1
    return answer


"""
- 분류: 수학
- 소요 시간: 15분
"""
