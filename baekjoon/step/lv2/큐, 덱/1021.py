# 회전하는 큐
# 출처1: https://velog.io/@goplanit/Algorithm-백준-1021번-회전하는-큐파이썬
# 출처2: https://jae-eun-ai.tistory.com/10
from collections import deque

N, M = map(int, input().split())
targets = list(map(int, input().split()))
q = deque(range(1, N + 1))
answer = 0

for target in targets:
    while True:
        if q[0] == target:
            q.popleft()
            break
        else:
            # 핵심: 어느 방향으로 회전할지 간단히 판정 -> 인덱스가 큐의 절반을 넘는지 확인
            if q.index(target) <= len(q) // 2:
                q.append(q.popleft())  # 팁: deque.rotate()도 가능
            else:
                q.appendleft(q.pop())
            answer += 1

print(answer)

"""
- 난이도: 실버3
- 분류: 덱

- 덱을 활용한 풀이
"""
