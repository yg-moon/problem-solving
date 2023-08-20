def is_balanced(s):
    l_cnt = 0
    r_cnt = 0
    for char in s:
        if char == "(":
            l_cnt += 1
        elif char == ")":
            r_cnt += 1
    return l_cnt == r_cnt


def is_correct(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                return False
            elif stack[-1] == "(":
                stack.pop()
    return not stack


def solution(p):
    # 예외
    if is_correct(p):
        return p
    # 1.
    if not p:
        return p
    # 2.
    for i in range(2, len(p) + 1):
        u = p[:i]
        v = p[i:]
        if is_balanced(u) and is_balanced(v):
            # 3.
            if is_correct(u):
                return u + solution(v)
            # 4.
            else:
                ret = "("
                ret += solution(v)
                ret += ")"
                for char in u[1:-1]:
                    if char == "(":
                        ret += ")"
                    elif char == ")":
                        ret += "("
                return ret


"""
- 분류: 구현, 문자열, 스택
- 시간: 3:20-3:45 (25분)
"""
