from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            # (swap items)
            # ex. head = 1-2-3-4
            swapped_head = head.next  # swapped_head = 2-3-4
            head.next = swapped_head.next  # head = 1-3-4
            swapped_head.next = head  # swapped_head = 2-1-3-4

            # (prev -> swapped list)
            prev.next = swapped_head

            # Move for next iteration
            head = head.next  # Not head.next.next
            prev = prev.next.next

        return root.next
