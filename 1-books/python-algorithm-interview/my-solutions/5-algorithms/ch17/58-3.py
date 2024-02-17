# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 연결리스트 -> 배열
        cur = head
        lst = []
        while cur:
            lst.append(cur.val)
            cur = cur.next

        # 정렬
        lst.sort()

        # 배열 -> 연결리스트
        cur = head
        for i in range(len(lst)):
            cur.val = lst[i]
            cur = cur.next

        return head
