# 등수 매기기
import sys, heapq

input = sys.stdin.readline

pq = []

N = int(input())
for _ in range(N):
    x = int(input())
    heapq.heappush(pq, x)

rank = 1
answer = 0
for _ in range(N):
    x = heapq.heappop(pq)
    answer += abs(rank - x)
    rank += 1

print(answer)

"""
- 난이도: 실버3
- 분류: 그리디

풀이
- 우선순위 큐: 매번 가장 낮은 예상등수를 뽑고, 현재 등수와의 차이를 불만도에 추가
- (사실 이 문제는 그냥 정렬해서 풀어도 되긴함)
"""
