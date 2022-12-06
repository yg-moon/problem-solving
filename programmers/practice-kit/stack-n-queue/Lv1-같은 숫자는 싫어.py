def solution(arr):
    stack = []
    for x in arr:
        if not stack:
            stack.append(x)
        else:
            if stack[-1] != x:
                stack.append(x)
    return stack


"""
- 첫 숫자는 일단 스택에 push.
- 매번 현재 숫자가 스택의 top과 다를때만 push.
- 그대로 스택을 리턴하면 정답.
"""
