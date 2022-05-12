import heapq
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        # 키를 기준으로 max heap 생성
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        # 순서대로 뽑으며, 두번째 값의 인덱스에 삽입
        while heap:
            person = heapq.heappop(heap)
            # 이렇게 하면 원하는 인덱스에 삽입후 나머지 밀어내기 가능
            result.insert(person[1], [-person[0], person[1]])
        return result
