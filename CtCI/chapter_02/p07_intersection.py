from chapter_02.linked_list import LinkedList, LinkedListNode


def intersection(list1, list2):
    if list1.tail is not list2.tail:
        return False

    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list1) < len(list2) else list1

    diff = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    for _ in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


def my_sol(l1, l2):
    def get_len(node):
        if not node:
            return 0
        else:
            return get_len(node.next) + 1

    h1 = l1.head
    h2 = l2.head
    len1 = get_len(h1)
    len2 = get_len(h2)

    if len1 < len2:
        h1, h2 = h2, h1  # 항상 h1이 더 길도록 설정

    for _ in range(abs(len1 - len2)):
        h1 = h1.next

    while h1 and h2:
        if h1 == h2:
            return h1
        h1 = h1.next
        h2 = h2.next


def test_linked_list_intersection():
    shared = LinkedList()
    shared.add_multiple([1, 2, 3, 4])

    a = LinkedList([10, 11, 12, 13, 14, 15])
    b = LinkedList([20, 21, 22])

    a.tail.next = shared.head
    a.tail = shared.tail
    b.tail.next = shared.head
    b.tail = shared.tail

    # should be 1
    assert intersection(a, b).value == 1
    assert my_sol(a, b).value == 1


if __name__ == "__main__":
    test_linked_list_intersection()
