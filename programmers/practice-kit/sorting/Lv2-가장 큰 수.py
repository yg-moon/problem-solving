from functools import cmp_to_key


def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    return str(int("".join(numbers)))


"""
- 핵심: 모든 숫자를 문자열로 변환한 후, a+b > b+a 이면 a를 더 앞에 놓도록 정렬한다.
  - 해설: 결국 이어붙였을 때 더 큰 수를 원하는 것이니므로 직접 해보면 된다.
- 예외 처리: 결과가 “0000” 인 경우를 고려하여 int로 한번 변환한 후 다시 str으로 바꿔 리턴한다.
"""
