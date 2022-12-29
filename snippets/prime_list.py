# Sieve of Eratosthenes
def prime_list(n):
    arr = [True] * n

    for i in range(2, int(n**0.5) + 1):
        if arr[i] == True:  # i가 소수인 경우
            for j in range(i + i, n, i):  # i이후 i의 배수들을 False 판정
                arr[j] = False

    return [i for i in range(2, n) if arr[i] == True]
