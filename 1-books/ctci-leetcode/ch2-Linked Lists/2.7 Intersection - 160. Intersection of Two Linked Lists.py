from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 핵심: 길이를 재고 차이만큼 당긴 후, 같은 노드가 나올때까지 탐색
    # O(N+M) time, O(1) space
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # 길이 재기
        lenA = 0
        lenB = 0
        ptr1 = headA
        ptr2 = headB
        while ptr1:
            lenA += 1
            ptr1 = ptr1.next
        while ptr2:
            lenB += 1
            ptr2 = ptr2.next

        # 차이만큼 당기기
        ptr1 = headA
        ptr2 = headB
        if lenA <= lenB:
            for _ in range(lenB - lenA):
                ptr2 = ptr2.next
        else:
            for _ in range(lenA - lenB):
                ptr1 = ptr1.next

        # 같은 노드 찾기
        while ptr1 and ptr2:
            if ptr1 == ptr2:
                return ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next

    # Sol. 길이를 재지 않고 해결
    # 핵심: 끝에 도달했을때 상대방의 head로 이동하면, 두번째 반복에서 만나게 됨
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        a = headA
        b = headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a


"""
- 난이도: Easy (Follow-up: Medium)
- 분류: 연결리스트
"""
