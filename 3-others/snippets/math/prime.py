# 효과적인 소수 판별 알고리즘: 제곱근까지만 판별하면 된다.
# 이유: 모든 약수는 가운데 수를 기준으로 ‘곱셈 연산에 대해 대칭’을 이루는 성질이 있기 때문.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 에라토스테네스의 체
def prime_list(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(n**0.5) + 1):
        if arr[i]:
            # 핵심: i*2부터 n까지, i씩 증가하며 처리
            for j in range(i * 2, n + 1, i):
                arr[j] = False

    return [i for i in range(n + 1) if arr[i]]
