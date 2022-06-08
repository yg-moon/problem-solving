# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 초기값 변경
        curr = root = ListNode(0)
        while head:
            while curr.next and curr.next.val < head.val:
                curr = curr.next

            curr.next, head.next, head = head, curr.next, head.next

            # 필요한 경우에만 cur 포인터가 되돌아가도록 처리
            if head and curr.val > head.val:
                curr = root
        return root.next
