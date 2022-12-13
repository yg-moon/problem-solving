import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while len(scoville) >= 2 and scoville[0] < K:
        item1 = heapq.heappop(scoville)
        item2 = heapq.heappop(scoville)
        new_item = item1 + item2 * 2
        heapq.heappush(scoville, new_item)
        cnt += 1

    if scoville[0] < K:
        return -1
    return cnt


"""
- 2개씩 빼서 연산하고, 결과를 다시 삽입 (힙을 이용한 대표적인 풀이)
"""
