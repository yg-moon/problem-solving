# 괄호의 값
s = input()


# 올바른 괄호열인지 확인
def is_correct():
    stack = []

    for c in s:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif c == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        else:
            return False

    # 주의: 끝났는데 스택이 비지 않았으면 불가능!
    if stack:
        return False

    return True


if not is_correct():
    print(0)
    exit()


def solve():
    stack = []

    for c in s:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if stack[-1] == "(":
                stack.pop()
                tmp = 2
            elif stack[-1].isdigit():
                tmp = int(stack.pop()) * 2
                stack.pop()
            # 주의: 왼쪽에 숫자가 있는지 항상 한번 더 확인
            if stack and stack[-1].isdigit():
                tmp += int(stack.pop())
            stack.append(str(tmp))
        elif c == "]":
            if stack[-1] == "[":
                stack.pop()
                tmp = 3
            elif stack[-1].isdigit():
                tmp = int(stack.pop()) * 3
                stack.pop()
            if stack and stack[-1].isdigit():
                tmp += int(stack.pop())
            stack.append(str(tmp))

    print(int(stack[0]))


solve()

"""
- 난이도: 골드5
- 분류: 자료구조(스택)
- 소요 시간: 1시간 (풀이 30분, 디버깅 30분)

핵심
- ): 앞에 괄호면 2, 숫자면 *2
    -> 다시 앞에 숫자면 더하기
- ]: 앞에 괄호면 3, 숫자면 *3
    -> 다시 앞에 숫자면 더하기

디버깅: 틀렸습니다, 런타임에러
- 1. 왼쪽에 숫자가 있는지 항상 확인해주지 않았음
- 2. 올바른 괄호열인지 제대로 확인하지 않았음
"""
