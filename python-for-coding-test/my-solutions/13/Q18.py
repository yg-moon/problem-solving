# Kakao 2020
from collections import Counter


# 균형잡힌 괄호 문자열 검증: ( 와 ) 의 개수가 같으면.
def isBalanced(s):
    counter = Counter(s)
    if counter["("] == counter[")"]:
        return True
    return False


# 올바른 괄호 문자열 검증 방법: 스택 구현
def isCorrect(s):
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
        if isBalanced(p[0:i]):
            u = p[0:i]
            v = p[i:]
            # 3.
            if isCorrect(u):
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
