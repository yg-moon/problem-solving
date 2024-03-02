class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 핵심: 다음 노드의 값을 복사하고, 다음 노드를 지우기
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


"""
- 난이도: Medium
- 분류: 연결리스트
"""
