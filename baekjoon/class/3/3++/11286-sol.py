# 절댓값 힙
# 출처: https://hongcoding.tistory.com/77
import sys, heapq

input = sys.stdin.readline

heap = []

N = int(input())

for _ in range(N):
    x = int(input())
    if x != 0:
        # 핵심: (절댓값, 원래값)의 튜플을 넣어준다.
        heapq.heappush(heap, (abs(x), x))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])

"""
- 이렇게 훨씬 간단하게 구현할 수 있었다.

- 의문: 현재 구현에서 후보가 여러개일 때는 어떻게 항상 가장 작은 수를 출력하는게 보장되는지?
- 해답: (우선순위, 작업) 튜플은 우선순위가 같다면 작업의 기본 비교 순서대로 ‘느슨하게’ 정렬됨.
"""
