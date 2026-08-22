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

    # Sol1. 리스트 뒤집기
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        root = head = ListNode()
        carry = 0

        while l1 or l2 or carry:
            val1 = 0
            val2 = 0

            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next

            carry, val = divmod(val1 + val2 + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return self.reverseList(root.next)

    # Sol2. 스택
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        cur = ListNode()
        carry = 0

        while stack1 or stack2 or carry:
            val1 = 0
            val2 = 0

            if stack1:
                val1 = stack1.pop()
            if stack2:
                val2 = stack2.pop()

            carry, val = divmod(val1 + val2 + carry, 10)

            # 결과도 역순으로 생성하기
            cur.val = val
            head = ListNode(carry)
            head.next = cur
            cur = head

        if carry == 0:
            return cur.next
        else:
            return cur


"""
(연관 문제)
- 난이도: Medium
- 분류: 연결리스트
"""
