# A와 B
S = list(input())
T = list(input())

is_possible = False

while T:
    if T[-1] == "A":
        T.pop()
    elif T[-1] == "B":
        T.pop()
        T.reverse()
    if S == T:
        is_possible = True
        break

if is_possible:
    print(1)
else:
    print(0)

"""
- 난이도: 골드5
- 분류: 그리디

핵심: 역방향으로 생각하기 (T -> S가 가능한지)
- 1. 끝에 A가 있다면 제거
- 2. 끝에 B가 있다면 제거하고 뒤집기

디버깅: 시간초과
- 나이브한 방법으로 풀면 시간초과 (2^1000)

출처
- https://chocochip101.tistory.com/entry/백준-12904번-파이썬-A와-B
"""
