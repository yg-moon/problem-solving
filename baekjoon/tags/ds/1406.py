# 에디터
stack1 = list(input())
stack2 = []

M = int(input())

for _ in range(M):
    cmd = input().split()

    if cmd[0] == "L":
        if stack1:
            stack2.append(stack1.pop())
    elif cmd[0] == "D":
        if stack2:
            stack1.append(stack2.pop())
    elif cmd[0] == "B":
        if stack1:
            stack1.pop()
    elif cmd[0] == "P":
        stack1.append(cmd[1])

# 스택2는 뒤집어진 상태. 비어있는지 확인하고 처리.
if stack2:
    stack2.reverse()
    stack1.extend(stack2)

print("".join(stack1))

"""
- 난이도: 실버2
- 분류: 자료구조(스택)

- 핵심: 커서를 기준으로 문자열을 스택 2개에 나누어 담기
    - 이렇게 하면 모든 연산을 append, pop으로 처리하여 O(1)에 가능
- 디버깅: 단순 구현 풀이는 시간초과

- 참고: https://seongonion.tistory.com/53
"""
