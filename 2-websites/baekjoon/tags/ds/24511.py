# queuestack
from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

q = deque()
result = []

# 큐의 원소들만 모아서 시작
for i in range(N):
    if A[i] == 0:
        q.append(B[i])

# 하나씩 enqueue 하고 dequeue
for c in C:
    q.appendleft(c)
    result.append(q.pop())

print(*result)

"""
- 난이도: 실버3
- 분류: 자료구조

핵심
- 스택은 무시하고 큐만 사용 (문제구조상 가능)

디버깅: 시간초과
- O(N*M) 으로 시도했더니 10^10 이었기 때문
"""
