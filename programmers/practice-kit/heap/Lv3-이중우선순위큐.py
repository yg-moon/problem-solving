import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    cur_len = 0

    for op in operations:
        cmd, num = op.split()
        num = int(num)
        if cmd == "I":
            shared_obj = [num, True]  # 공유 객체
            heapq.heappush(min_heap, shared_obj)
            heapq.heappush(max_heap, [-num, shared_obj])
            cur_len += 1
        elif cmd == "D":
            if cur_len == 0:
                continue
            elif num == 1:
                while max_heap:
                    _, shared_obj = heapq.heappop(max_heap)
                    if shared_obj[1]:
                        shared_obj[1] = False
                        cur_len -= 1
                        break
            elif num == -1:
                while min_heap:
                    shared_obj = heapq.heappop(min_heap)
                    if shared_obj[1]:
                        shared_obj[1] = False
                        cur_len -= 1
                        break

    # 정답 출력
    if cur_len == 0:
        return [0, 0]
    elif cur_len == 1:
        while min_heap:
            num, valid = heapq.heappop(min_heap)
            if valid:
                return [num, num]
    else:
        while max_heap:
            _, [num, valid] = heapq.heappop(max_heap)
            if valid:
                max_num = num
                break
        while min_heap:
            num, valid = heapq.heappop(min_heap)
            if valid:
                min_num = num
                break
        return [max_num, min_num]


"""
- 요약: min heap, max heap을 함께 사용
- 구현
    - 핵심: 삭제 발생시 두 heap을 동기화 하는 방법
    - 반대쪽 힙은 실제로 삭제하지 않고 표시만 해두고, 현재 힙에서 삭제할때 invalid한 경우를 무시
        - ex. [num, True] 같은 형태로 저장하여 삭제가 되었을 경우 False로 표시
    - 공유 객체를 이용해서, 한쪽에서 값을 바꿀 경우 다른 힙에도 반영되도록 구현 (!)
        - (이렇게 하면 반대쪽 힙에서 해당 원소의 위치를 탐색할 필요가 없어짐)
"""
