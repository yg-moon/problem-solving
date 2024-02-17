import time
from chapter_02.linked_list import LinkedList


def remove_dups(ll):
    current = ll.head
    previous = None
    seen = set()

    while current:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    ll.tail = previous
    return ll


def remove_dups_followup(ll):
    run = cur = ll.head
    while cur:
        run = cur
        while run.next:
            if run.next.value == cur.value:
                run.next = run.next.next
            else:
                run = run.next
        cur = cur.next
    return ll


def my_sol(ll):
    cur = ll.head
    prev = None  # 직전 노드의 위치를 가리키는 포인터
    seen = set()

    while cur:
        if cur.value in seen:
            prev.next = cur.next
        else:
            seen.add(cur.value)
            prev = cur
        cur = cur.next

    return ll


testable_functions = (remove_dups, remove_dups_followup, my_sol)
test_cases = (
    ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 2], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
)


def test_remove_dupes():
    for f in testable_functions:
        start = time.perf_counter()
        for _ in range(100):
            for values, expected in test_cases:
                expected = expected.copy()
                deduped = f(LinkedList(values))
                assert deduped.values() == expected

        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    test_remove_dupes()

# Run with: python3 -m chapter_02.p01_remove_dups
