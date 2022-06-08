from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 처음 요소 넣기
        root = ListNode()
        root.next = head
        head = head.next
        root.next.next = None

        while head:
            prev = root
            curr = root.next
            while prev:
                if not curr:
                    next = head.next
                    head.next = None
                    prev.next = head
                    head = next
                    break
                if head.val < curr.val:
                    next = head.next
                    head.next = curr
                    prev.next = head
                    head = next
                    break
                else:
                    prev = curr
                    curr = curr.next

        return root.next
