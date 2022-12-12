from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 처음 노드는 일단 그냥 넣기
        root = ListNode()
        root.next = head
        head = head.next
        root.next.next = None

        while head:
            # 매번 맨앞에서 출발
            prev = root
            cur = root.next
            while prev:
                # 자신보다 큰 노드가 나오면 그 앞에 넣기
                # 끝까지 도착했으면 그냥 넣기
                if not cur or head.val < cur.val:
                    next = head.next  # 다음 진행할 노드를 저장
                    head.next = cur  # (경우에 따라 어떤 동작인지 다름)
                    prev.next = head  # 현재 노드를 결과에 이어붙이기
                    head = next  # 다음 진행할 노드 설정
                    break
                else:
                    prev = cur
                    cur = cur.next

        return root.next


"""
- 요약: 새로운 연결리스트를 만들어서 적절한 위치에 각 노드 넣기.
"""
