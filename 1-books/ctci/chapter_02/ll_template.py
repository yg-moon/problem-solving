# Class Definition
class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def add_mutiple(self, values):
        for v in values:
            self.add(v)

    def get_list(self):
        ret = []
        cur = self.head
        while cur:
            ret.append(cur.value)
            cur = cur.next
        return ret


# Solution
def my_sol(ll):
    return ll


# Driver Code
test_cases = [[], [1, 2, 3, 4], [1, 1, 1, 1, 1], [1, 2, 2, 3], [1, 2, 3, 2]]
for tc in test_cases:
    ll = LinkedList()
    ll.add_mutiple(tc)
    print(f"in  : {tc}")
    print(f"out : {my_sol(ll).get_list()}")
    print()
