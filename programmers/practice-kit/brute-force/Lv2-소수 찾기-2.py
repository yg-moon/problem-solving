from math import sqrt

prime_set = set()


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def makePermutations(str1, str2):
    if str1 != "" and isPrime(int(str1)):
        prime_set.add(int(str1))

    # 매번 str2의 문자 한개를 str1에 붙여주고, (현재 문자열, 남은 문자열)로 재귀
    for i in range(len(str2)):
        makePermutations(str1 + str2[i], str2[:i] + str2[i + 1 :])


def solution(numbers):
    makePermutations("", numbers)
    return len(prime_set)


"""
- 직접 모든 경우를 생성 (재귀 완전탐색)
"""
