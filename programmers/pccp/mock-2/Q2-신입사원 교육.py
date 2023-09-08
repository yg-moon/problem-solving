import heapq


def solution(ability, number):
    heapq.heapify(ability)

    for _ in range(number):
        x1 = heapq.heappop(ability)
        x2 = heapq.heappop(ability)
        heapq.heappush(ability, x1 + x2)
        heapq.heappush(ability, x1 + x2)

    return sum(ability)


"""
- 분류: 그리디, 우선순위 큐
- 시간: 10:45-10:50 (5분)
"""
