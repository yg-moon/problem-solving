# N번째 큰 수
import heapq

N = int(input())
pq = []

for _ in range(N):
    nums = map(int, input().split())
    for num in nums:
        heapq.heappush(pq, num)
        # 핵심: heap의 크기를 n개로 유지
        if len(pq) > N:
            heapq.heappop(pq)

print(pq[0])

"""
- 난이도: 실버2
- 분류: 자료구조(우선순위 큐)

- 요약: min heap에 n개만 저장하도록 유지하면, 종료시 (n번째로 큰 수 ~ 가장 큰 수)가 남음
- 참고: https://codejin.tistory.com/215
"""
