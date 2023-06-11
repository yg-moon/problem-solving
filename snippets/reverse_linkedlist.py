class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head):
    prev = None
    cur = head
    while cur:
        next_node = cur.next  # save next node
        cur.next = prev  # add current node to the left of prev
        prev = cur  # change the prev pointer
        cur = next_node  # move on to next node
    return prev
