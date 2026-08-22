from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    # 핵심: 가운데를 찾아서 뒤집고, 절반씩 비교
    # O(N) time, O(1) space
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # 가운데 찾기
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 뒤집기
        rev_head = self.reverseList(slow)

        # 절반씩 비교
        while rev_head:
            if rev_head.val != head.val:
                return False
            rev_head = rev_head.next
            head = head.next
        return True


"""
- 난이도: Easy (Follow-up: Medium)
- 분류: 연결리스트
"""
