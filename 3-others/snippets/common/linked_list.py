class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# LeetCode 206
def reverseList(head):
    prev = None
    cur = head

    while cur:
        next_node = cur.next  # 1. 다음 노드 임시저장
        cur.next = prev  # 2. 현재 노드의 포인터를 이전 노드로 변경
        prev = cur  # 3. prev 포인터 업데이트
        cur = next_node  # 4. 다음 노드로 이동

    return prev


def reverseList_rec(cur, prev=None):
    if not cur:
        return prev

    next_node = cur.next  # 1. 다음 노드를 임시 저장
    cur.next = prev  # 2. 현재 노드의 포인터를 이전 노드로 변경
    return reverseList_rec(next_node, cur)  # 3, 4


def get_len_rec(node):
    if not node:
        return 0
    else:
        return get_len_rec(node.next) + 1


def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("End")


# Driver Code
head = ListNode(1, ListNode(2, ListNode(3)))

print_list(head)
print(get_len_rec(head))

head = reverseList(head)
print_list(head)

head = reverseList_rec(head)
print_list(head)
