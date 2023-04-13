# 단어 뒤집기 2
S = input()

tag_stack = []
word_stack = []
result = []
is_tag = False

for s in S:
    if s == "<":
        is_tag = True
        tag_stack.append(s)
        if word_stack:
            result.append("".join(word_stack[::-1]))
            word_stack.clear()
    elif s == ">":
        is_tag = False
        tag_stack.append(s)
        result.append("".join(tag_stack))
        tag_stack.clear()
    else:
        if is_tag:
            tag_stack.append(s)
        # 태그가 아닌 단어일 경우
        else:
            if s == " ":
                result.append("".join(word_stack[::-1]))
                word_stack.clear()
                result.append(s)
            else:
                word_stack.append(s)

# 주의: 스택 문제는 항상 마지막에 남은거 비워주기
if word_stack:
    result.append("".join(word_stack[::-1]))

print("".join(result))

"""
- 난이도: 실버3
- 분류: 문자열, 스택

- 스택이라는 풀이에 매몰돼서 지나치게 복잡해진 풀이.
"""
