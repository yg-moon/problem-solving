# 요세푸스 문제 0
# 출처: https://hongcoding.tistory.com/41
from collections import deque

N, K = map(int, input().split())
q = deque()
answer = []

for i in range(1, N + 1):
    q.append(i)

# 핵심: k-1번만큼 (popleft + append)하고, 한번 더 popleft.
while q:
    for i in range(K - 1):
        q.append(q.popleft())
    answer.append(q.popleft())

print("<", end="")
for i in range(len(answer) - 1):
    print(f"{answer[i]}, ", end="")
print(answer[-1], end="")
print(">")

"""
- 큐를 사용한 풀이
"""
