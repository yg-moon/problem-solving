import heapq

N = int(input())

heap = []
for i in range(N):
    num = int(input())
    heapq.heappush(heap, num)

total = 0
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    # 전체 누적값과 현재 합을 계산
    sum_val = first + second
    total += sum_val
    # 합친 카드 묶음을 다시 삽입
    heapq.heappush(heap, sum_val)

print(total)
