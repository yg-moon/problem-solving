class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head):
    cur = head
    prev = None

    while cur:
        next_node = cur.next  # 1.다음 노드 저장
        cur.next = prev  # 2.prev의 좌측에 현재 노드를 달기
        prev = cur  # 3.prev 위치 업데이트
        cur = next_node  # 4.다음 노드로 이동

    return prev


def get_len(node):
    if not node:
        return 0
    else:
        return get_len(node.next) + 1
