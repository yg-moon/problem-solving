# 오등큰수
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

F = defaultdict(int)
for a in A:
    F[a] += 1

stack = []
answer = [-1] * N
for i in range(N):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)

"""
- 난이도: 골드3
- 분류: 스택

- 오큰수에서 비교조건만 달라진 문제
"""
