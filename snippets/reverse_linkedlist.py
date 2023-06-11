class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head):
    prev = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev
