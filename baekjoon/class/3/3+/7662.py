# 이중 우선순위 큐
# 출처: https://hongcoding.tistory.com/92
import heapq, sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    valid = [False] * k  # 핵심: 삭제된 요소를 하나의 공통배열을 통해 관리

    for i in range(k):
        op, num = input().split()
        if op == "I":
            heapq.heappush(min_heap, (int(num), i))  # 핵심: 인덱스도 힙에 넣어주기
            heapq.heappush(max_heap, (-int(num), i))
            valid[i] = True
        else:
            if num == "-1":
                # 다른 힙에서 이미 삭제된 노드를 모두 제거
                while min_heap and not valid[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                # 현재 힙에서 노드를 삭제
                if min_heap:
                    valid[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            else:
                while max_heap and not valid[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    valid[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    # 남아있는 불필요한 노드를 모두 제거
    while min_heap and not valid[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not valid[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")

"""
- 난이도: 골드4
- 분류: 우선순위 큐

- 삭제된 요소를 동기화 하는게 중요한 것은 같지만, 구현 방법이 다르다.
    - 고득점 kit 풀이처럼 공유객체를 사용하는게 아니라, valid 배열을 통해 관리한다.
- valid 배열을 사용한 것만 중요한게 아니라, 인덱스도 힙에 같이 넣어주는 것이 포인트.
"""
