# 도키도키 간식드리미
N = int(input())
arr = list(map(int, input().split()))

arr.reverse()

is_ok = True
target = 1
stack = []

while target <= N:
    if arr and arr[-1] == target:
        arr.pop()
        target += 1
    elif stack and stack[-1] == target:
        stack.pop()
        target += 1
    else:
        if arr:
            item = arr.pop()
            if stack and stack[-1] < item:
                is_ok = False
                break
            else:
                stack.append(item)
        else:
            is_ok = False
            break

print("Nice") if is_ok else print("Sad")

"""
- 난이도: 실버3
- 분류: 자료구조(스택)

요약
- 매번 두 줄을 모두 확인하기
    - 현재 간식 받아야 할 사람이면 pop으로 빼냄
    - 아니라면 한명씩만 설 수 있는 공간으로 보내는데, 기존의 마지막 숫자보다 크면 실패
"""
