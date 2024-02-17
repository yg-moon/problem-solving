from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ex. 1 -> 2 -> 3 -> 4
        if head and head.next:
            p = head.next  # p = 2
            head.next = self.swapPairs(p.next)  # 1.next = swapPairs(3)
            p.next = head  # 2.next = 1
            return p  # p = 2 -> 1 -> swapPairs(3)

        return head
