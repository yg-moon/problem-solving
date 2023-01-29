# 요세푸스 문제 0
# 출처: https://hongcoding.tistory.com/41
from collections import deque

N, K = map(int, input().split())
q = deque([x for x in range(1, N + 1)])
answer = []

# 핵심: k-1번만큼 (popleft + append)하고, 한번 더 popleft 한 것을 정답에 추가.
while q:
    for _ in range(K - 1):
        q.append(q.popleft())
    answer.append(q.popleft())

print("<", end="")
for i in range(len(answer) - 1):
    print(f"{answer[i]}, ", end="")
print(f"{answer[-1]}>")

"""
- 큐를 사용한 풀이
"""
