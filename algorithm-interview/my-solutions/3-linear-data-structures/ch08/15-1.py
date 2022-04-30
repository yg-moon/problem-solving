from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 보조함수 작성
        def reverse(node: Optional[ListNode], prev: Optional[ListNode] = None):
            if not node:  # <=> while head:
                return prev
            next = node.next  # 1.next 저장
            node.next = prev  # 2.prev 왼쪽에 하나 더 달기
            return reverse(next, node)  # 4.다음 칸으로 이동, 3.prev 정보 최신화

        return reverse(head)
