# 후위 표기식
# 출처: https://pannchat.tistory.com/entry/파이썬-백준-후위표기식-python
infix = list(input())
stack = []
answer = ""

for x in infix:
    # 피연산자가 들어오면: 바로 결과에 추가
    if x.isalpha():
        answer += x
    else:
        # 여는 괄호를 만나면: 무조건 스택에 담음
        if x == "(":
            stack.append(x)
        # 연산자가 들어오면:
        # - 1. 자신보다 우선순위가 높거나 같은 것들을 모두 스택에서 뽑아 결과에 추가
        # - 2. 자신을 스택에 추가
        elif x == "*" or x == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                answer += stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":
            while stack and stack[-1] != "(":  # 여는 괄호 직전까지만
                answer += stack.pop()
            stack.append(x)
        # 닫는 괄호를 만나면: 여는 괄호를 만날 때까지 스택에서 뽑아 결과에 추가
        elif x == ")":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()  # 여는 괄호 제거

# 마지막으로 스택에 남아있는 내용들을 결과에 추가
while stack:
    answer += stack.pop()

print(answer)

"""
- 난이도: 골드2
- 분류: 스택

동작 요약
- 1. 피연산자는 결과에 바로 추가.
- 2. 괄호와 연산자는 스택에 쌓고, 조건이 맞으면 스택에 있는 연산자를 결과에 추가.

추가 설명
- https://subin-0320.tistory.com/73
- https://kyun2da.github.io/2021/05/13/postfix_notation/
"""
