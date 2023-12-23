# 쇠막대기
s = input()
stack = []
answer = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    elif s[i] == ")":
        # 레이저인 경우
        if s[i - 1] == "(":
            stack.pop()
            answer += len(stack)
        # 막대의 끝인 경우
        else:
            stack.pop()
            answer += 1

print(answer)

"""
- 난이도: 실버2
- 분류: 자료구조(스택)

핵심
- 앞에 무엇이 있는지로 똑같은 ')'를 레이저 또는 막대로 구분
- 레이저일때: '('를 pop하고 여태 스택에 쌓인 크기만큼 정답에 더하기
- 막대일때: 한개를 pop하고 1만큼 정답에 더하기

- 참고: https://chan9.tistory.com/39
"""
