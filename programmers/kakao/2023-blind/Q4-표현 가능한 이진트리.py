def full_bin(s):
    idx = 2
    while len(s) > idx - 1:
        idx *= 2
    ret = "0" * (idx - 1 - len(s)) + s
    return ret


def is_all_zero(s):
    for char in s:
        if char != "0":
            return False
    return True


def can_draw(s):
    if len(s) == 1 or is_all_zero(s):
        return True

    mid_idx = len(s) // 2
    left = s[:mid_idx]
    right = s[mid_idx + 1 :]

    return s[mid_idx] == "1" and can_draw(left) and can_draw(right)


def solution(numbers):
    answer = []

    for num in numbers:
        answer.append(int(can_draw(full_bin(bin(num)[2:]))))

    return answer


"""
- 분류: 트리, 분할정복
- 출처: https://algosu.tistory.com/152

핵심
- 1. 주어진 정수를 포화 이진수로 변경: 길이가 2^N-1이 될때까지 앞쪽을 0으로 채움
- 2. 트리를 분할정복해서 가능한 경우인지 확인
    - 부모가 1인 경우: 왼쪽 서브트리, 오른쪽 서브트리에 문제가 없다면 가능
    - 부모가 0인 경우: 자식들이 모두 0인 경우에만 가능
"""
