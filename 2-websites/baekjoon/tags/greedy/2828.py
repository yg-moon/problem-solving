# 사과 담기 게임
N, M = map(int, input().split())
J = int(input())
apples = []

for _ in range(J):
    x = int(input())
    apples.append(x)

l = 1
r = M
answer = 0

for a in apples:
    while True:
        if l <= a <= r:
            break
        if a < l:
            l -= 1
            r -= 1
            answer += 1
        elif a > r:
            l += 1
            r += 1
            answer += 1

print(answer)

"""
- 난이도: 실버4
- 분류: 그리디

투포인터로 풀었음
"""
