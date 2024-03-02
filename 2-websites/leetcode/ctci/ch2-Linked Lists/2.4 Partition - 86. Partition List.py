from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 핵심: 리스트 2개를 만들고 연결
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = ListNode()
        head2 = ListNode()
        ptr1 = head1
        ptr2 = head2

        while head:
            if head.val < x:
                ptr1.next = head
                ptr1 = ptr1.next
            else:
                ptr2.next = head
                ptr2 = ptr2.next
            head = head.next

        ptr2.next = None  # 주의: 사이클 방지
        ptr1.next = head2.next

        return head1.next


"""
- 난이도: Medium
- 분류: 연결리스트
"""
