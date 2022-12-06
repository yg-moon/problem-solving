def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    return True


"""
- '('를 만나면: 스택에 push
- ')'를 만나면: 스택에서 pop (이때 스택이 비어있으면 짝이 틀림)
- 모든 작업 이후에도 스택에 내용물이 남아있다면 짝이 틀림.
"""
