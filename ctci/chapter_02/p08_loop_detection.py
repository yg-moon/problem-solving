from chapter_02.linked_list import LinkedList


def loop_detection(ll):
    slow = fast = ll.head

    # collision spot 찾기
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # 예외처리: 루프가 없는 경우
    if not fast or not fast.next:
        return None

    # 루프의 시작점 찾기
    slow = ll.head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


def test_loop_detection():
    looped_list = LinkedList(["A", "B", "C", "D", "E"])
    loop_start_node = looped_list.head.next.next
    looped_list.tail.next = loop_start_node
    tests = [
        (LinkedList(), None),
        ((LinkedList((1, 2, 3))), None),
        (looped_list, loop_start_node),
    ]

    for ll, expected in tests:
        assert loop_detection(ll) == expected


if __name__ == "__main__":
    test_loop_detection()
