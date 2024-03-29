# BOJ 1715
# 출처: 이코테
import heapq

N = int(input())

heap = []
for i in range(N):
    num = int(input())
    heapq.heappush(heap, num)

answer = 0
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)

    # 전체 누적값과 현재 합을 계산
    temp_sum = first + second
    answer += temp_sum

    # 합친 카드 묶음을 다시 삽입
    heapq.heappush(heap, temp_sum)

print(answer)
