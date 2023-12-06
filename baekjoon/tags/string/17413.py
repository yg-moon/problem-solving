# 단어 뒤집기 2
# 출처: https://star7sss.tistory.com/391
S = input()

stack = []
is_tag = False
answer = ""

for s in S:
    # < 를 만나면 스택을 비움
    if s == "<":
        while stack:
            answer += stack.pop()
        is_tag = True
        answer += s

    elif s == ">":
        is_tag = False
        answer += s

    # 공백이면 스택을 비움
    # (태그 내부의 공백일 경우, 항상 스택이 비어있을 것이므로 상관없음)
    elif s == " ":
        while stack:
            answer += stack.pop()
        answer += s

    # 태그 내부의 글자는 바로 정답에 추가
    elif is_tag:
        answer += s

    # 태그 외부의 단어는 뒤집기 위해 스택에 넣음
    else:
        stack.append(s)

# 남은거 처리
while stack:
    answer += stack.pop()

print(answer)

"""
- 난이도: 실버3
- 분류: 문자열, 스택

- 스택 하나만 사용한 간단한 풀이.
"""
