from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # 예외처리
        if head is None or left == right:
            return head

        # start: 처음 end의 한칸 왼쪽 노드
        # end: [left]에 해당하는 노드
        root = prev = ListNode(None)
        root.next = head
        for _ in range(left - 1):
            prev = prev.next
        left_node = prev.next

        for _ in range(right - left):
            rev_head = prev.next
            new_head = left_node.next
            left_node.next = left_node.next.next
            prev.next = new_head
            new_head.next = rev_head

        return root.next
