class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# LeetCode 206
def reverseList(head):
    prev = None

    while head:
        temp = head.next  # 1.다음 노드 임시저장
        head.next = prev  # 2.prev의 좌측에 현재 노드를 달기
        prev = head  # 3.prev 위치 업데이트
        head = temp  # 4.다음 노드로 이동

    return prev


def get_len(node):
    if not node:
        return 0
    else:
        return get_len(node.next) + 1
