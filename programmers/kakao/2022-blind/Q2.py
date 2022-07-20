def solution(n, k):
    # 숫자 n을 k 진수로 바꾸기
    num = []
    while n >= k:
        q, r = divmod(n, k)
        num.append(str(r))
        n = q
    num.append(str(n))
    num = "".join(num[::-1])

    # 소수 판별
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # 조건에 맞는 소수 개수 찾기
    count = 0
    num = num.split("0")
    for n in num:
        if n != "" and isPrime(int(n)):
            count += 1
    return count
