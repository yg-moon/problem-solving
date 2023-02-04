def solution(arr):
    stack = []

    for x in arr:
        # 첫 숫자는 일단 스택에 push
        if not stack:
            stack.append(x)
        else:
            # 매번 현재 숫자가 스택의 top과 다를때만 push
            if stack[-1] != x:
                stack.append(x)

    # 그대로 스택을 리턴하면 정답
    return stack
