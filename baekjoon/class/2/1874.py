# 스택 수열
import sys

input = sys.stdin.readline

stack = []
answer = []
i = 1
no_answer = False

n = int(input())

for _ in range(n):
    # 매 정수에 대해 확인하며
    cur = int(input())
    # 스택이 비었거나, 스택의 top이 현재 정수보다 작다면
    if not stack or stack[-1] < cur:
        # 현재 정수까지 모든 수를 스택에 push
        while i <= cur:
            stack.append(i)
            i += 1
            answer.append("+")
    # 스택의 top이 현재 정수와 일치하면 pop
    if stack and stack[-1] == cur:
        stack.pop()
        answer.append("-")
    # 여기까지 했는데 현재 정수를 찾을 수 없다면 불가능
    else:
        no_answer = True

if no_answer:
    print("NO")
else:
    for a in answer:
        print(a)

"""
- 난이도: 실버2
- 분류: 스택
"""
