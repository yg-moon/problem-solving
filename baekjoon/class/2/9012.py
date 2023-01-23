# 괄호
def is_balanced(string):
    stack = []
    for s in string:
        if s == "(":
            stack.append(s)
        elif s == ")":
            # 주의: 스택이 비었는지 확인
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    # 끝났는데도 스택이 비어있지 않다면 균형이 맞지 않음
    if stack:
        return False
    return True


N = int(input())

for _ in range(N):
    ps = input()
    if is_balanced(ps):
        print("YES")
    else:
        print("NO")

"""
- 난이도: 실버4
- 분류: 스택

- 기본적인 괄호 검증
"""
