from functools import cmp_to_key

# a+b > b+a 이면 a를 더 앞에 놓도록 정렬
def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1


def solution(numbers):
    numbers = list(map(str, numbers))  # 모든 숫자를 문자열로 변환
    numbers.sort(key=cmp_to_key(compare))  # 사용자 지정 기준으로 비교
    return str(int("".join(numbers)))  # 예외 처리: 결과가 “0000”인 경우를 고려
