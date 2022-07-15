# 출처: https://programmers.co.kr/learn/courses/30/lessons/42839/solution_groups?language=python3
from math import sqrt

primeSet = set()

# 제곱근까지만 판별하면 된다.
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 모든 permutation을 생성하고, set으로 관리하여 중복을 거르기.
def makePermutations(str1, str2):
    if str1 != "" and isPrime(int(str1)):
        primeSet.add(int(str1))

    # 매번 str2의 문자 한개를 str1에 붙여주고, (현재 문자열, 남은 문자열)로 재귀
    for i in range(len(str2)):
        makePermutations(str1 + str2[i], str2[:i] + str2[i + 1 :])


def solution(numbers):
    makePermutations("", numbers)
    answer = len(primeSet)
    return answer
