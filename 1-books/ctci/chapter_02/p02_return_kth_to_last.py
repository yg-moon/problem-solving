from chapter_02.linked_list import LinkedList


def kth_to_last(ll, k):
    leader = follower = ll.head
    count = 0

    while leader:
        if count >= k:
            follower = follower.next
        count += 1
        leader = leader.next
    return follower


# O(N) space
def kth_last_recursive(ll, k):
    head = ll.head
    cnt = 0

    def helper(node, k):
        nonlocal cnt
        # 1.base case
        if not node:
            return None
        # 2.DFS
        res = helper(node.next, k)
        # 3.return
        cnt = cnt + 1
        if cnt == k:
            return node
        return res

    return helper(head, k)


def my_sol(ll, k):
    slow = fast = ll.head

    for _ in range(k - 1):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    return slow


test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)


def test_kth_to_last():
    for linked_list_values, k, expected in test_cases:
        ll = LinkedList(linked_list_values)
        assert kth_to_last(ll, k).value == expected
        assert kth_last_recursive(ll, k).value == expected
        assert my_sol(ll, k).value == expected


if __name__ == "__main__":
    test_kth_to_last()
