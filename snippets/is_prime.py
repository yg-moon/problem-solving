from math import sqrt


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


"""
- 효과적인 소수 판별 알고리즘: 제곱근까지만 판별하면 된다.
  - 이유: 모든 약수는 가운데 수를 기준으로 ‘곱셈 연산에 대해 대칭’을 이루는 성질이 있기 때문.

- 팁: sqrt() 대신 int(n**0.5) 도 가능하다.
"""
