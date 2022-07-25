from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: when n = 0
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        # Separate odd and even nodes
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        # Add even's head to odd's tail
        odd.next = even_head

        return head
