# Kakao 2020
# 세부 구현이 조금 다름
from collections import Counter


# 균형잡힌 문자열: 각 괄호의 개수가 같으면
def is_balanced(s):
    counter = Counter(s)
    if counter["("] == counter[")"]:
        return True
    return False


# 올바른 괄호 문자열: 스택으로 확인
def is_correct(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True


def solution(p):
    # 1.
    if p == "":
        return p
    # 2.
    for i in range(2, len(p) + 1, 2):
        u = p[0:i]
        v = p[i:]
        if is_balanced(u) and is_balanced(v):
            # 3.
            if is_correct(u):
                # 3-1.
                return u + solution(v)
            # 4.
            else:
                # 4-1.
                result = "("
                # 4-2.
                result += solution(v)
                # 4-3.
                result += ")"
                # 4-4.
                temp = ""
                for char in u[1 : len(u) - 1]:
                    if char == "(":
                        temp += ")"
                    else:
                        temp += "("
                result += temp
                # 4-5.
                return result
