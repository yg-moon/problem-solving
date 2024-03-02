class Solution:
    # 핵심
    # - 사이클 내부의 노드를 하나 찾기 (slow와 fast가 만나는 지점)
    # - head에서부터 함께 출발하여 처음 만나는 지점이 순환 부분의 첫 노드(!)
    # O(1) space
    def detectCycle(self, head):
        if not head or not head.next:
            return None

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != head:
                    slow = slow.next
                    head = head.next
                return head

        return None


"""
- 난이도: Medium
- 분류: 연결리스트
"""
