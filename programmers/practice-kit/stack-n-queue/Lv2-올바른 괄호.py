def solution(s):
    stack = []

    for c in s:
        # '('를 만나면: 스택에 push
        if c == "(":
            stack.append(c)
        # ')'를 만나면: 스택에서 pop
        elif c == ")":
            # 이때 스택이 비어있으면 짝이 틀린것
            if not stack:
                return False
            else:
                stack.pop()

    # 모든 작업 이후에도 스택에 내용물이 남아있다면 짝이 틀린것
    if stack:
        return False
    return True
