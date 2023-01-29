# IOIOI
# 출처: https://black-hair.tistory.com/135
N = int(input())
M = int(input())
S = input()

i = cnt = answer = 0

while i <= (M - 3):
    if S[i : i + 3] == "IOI":
        cnt += 1
        i += 2
        if cnt == N:
            answer += 1
            cnt -= 1
    else:
        cnt = 0
        i += 1


print(answer)

"""
- 난이도: 실버1
- 분류: 문자열

요약
- IOI가 몇 번 연속되는지 갯수만 찾아서 체크한다.
- IOI가 발견되면 index를 2개 이동하고, 아닌 경우에는 index를 1개 이동하면서 검사한다.
"""
