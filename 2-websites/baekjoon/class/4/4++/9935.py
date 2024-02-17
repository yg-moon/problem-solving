# 문자열 폭발
# 출처: https://velog.io/@heejun32/백준-9935번-문자열-폭발-Python
string = input()
bomb = input()

stack = []
len_b = len(bomb)

# 스택에 한글자씩 넣으면서 매번 확인하며, 스택 끝에서 폭발 문자열이 발견되면 그 길이만큼 pop
for char in string:
    stack.append(char)
    if "".join(stack[-len_b:]) == bomb:
        for _ in range(len_b):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")

"""
- 난이도: 골드4
- 분류: 문자열, 스택

핵심
- 전체 문자열 길이는 <= 100만 이므로 전체를 split, join 하면 시간초과가 발생한다.
- 폭발 문자열의 길이는 <= 36 이므로, 그 길이만큼만 join 하는 현재 풀이는 시간내로 통과한다.
"""
