from itertools import permutations


def calc_one(l, op, r):
    if op == "+":
        return l + r
    elif op == "-":
        return l - r
    elif op == "*":
        return l * r


def calc_all(tokens, op):
    # 핵심2: 원하는 연산자의 앞뒤로 토큰을 계산하고 결과를 업데이트
    i = 0
    while i < len(tokens):
        if tokens[i] == op:
            result = calc_one(int(tokens[i - 1]), tokens[i], int(tokens[i + 1]))
            tokens[i - 1 : i + 2] = [str(result)]
        else:
            i += 1
    return tokens


def solution(expression):
    # 핵심1: 전체 문자열을 숫자와 연산자로 구분해서 토큰화
    tokens = []
    num = ""
    for char in expression:
        if char in ["+", "-", "*"]:
            if num:
                tokens.append(num)
                num = ""
            tokens.append(char)
        else:
            num += char
    if num:
        tokens.append(num)

    # 모든 연산자 우선순위에 대해 결과 계산
    answer = 0
    for perm in permutations(["+", "-", "*"], 3):
        tmp_tokens = tokens.copy()
        for op in perm:
            tmp_tokens = calc_all(tmp_tokens, op)
        answer = max(answer, abs(int(tmp_tokens[0])))
    return answer


"""
- 분류: 구현, 문자열, 완전탐색
"""
