# 국회의원 선거
import heapq

N = int(input())

pq = []
answer = 0

for i in range(N):
    if i == 0:
        dasom = int(input())
    else:
        heapq.heappush(pq, -int(input()))  # 주의: append로 쓰면 틀림

while pq:
    max_item = -heapq.heappop(pq)
    if max_item < dasom:
        break
    else:
        max_item -= 1
        dasom += 1
        answer += 1
        heapq.heappush(pq, -max_item)

print(answer)

"""
- 난이도: 실버5
- 분류: 그리디

핵심
- 다솜 제외 나머지를 pq에 넣고, 최대원소가 다솜보다 작을때까지 1씩 빼기
"""
