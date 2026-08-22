from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 핵심: 포인터 2개를 n개의 거리를 두고 출발
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head

        for _ in range(n):
            ptr2 = ptr2.next

        # 팁: 이렇게 예외처리하면 root를 안쓰고 깔끔하게 풀이 가능
        if not ptr2:
            return head.next

        # 끝까지 이동
        while ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        # 노드 삭제
        ptr1.next = ptr1.next.next

        return head


"""
(유사 문제)
- 난이도: Medium
- 분류: 연결리스트
"""
