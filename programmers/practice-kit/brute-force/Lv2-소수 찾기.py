from itertools import permutations


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    cnt = 0
    seen = set()

    # 조합의 길이를 1부터 입력값의 크기까지 늘려가면서 모든 경우를 확인.
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num = int("".join(p))
            if num not in seen and is_prime(num):
                cnt += 1
                seen.add(num)

    return cnt


"""
- permutations로 모든 경우를 찾고, 소수인지 확인하여 카운트를 추가.
"""
