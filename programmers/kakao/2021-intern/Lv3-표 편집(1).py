# 링크드 리스트 풀이
def solution(n, k, cmd):
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.prev = None
            self.next = None

    # 링크드리스트 생성
    root = curr = ListNode(0)
    for i in range(1, n):
        curr.next = ListNode(i)
        curr.next.prev = curr
        curr = curr.next

    # 주어진 시작 위치로 이동
    curr = root
    for i in range(k):
        curr = curr.next

    # cmd 처리
    removed = []
    for c in cmd:
        if c[0] == "U":
            for _ in range(int(c[2:])):
                curr = curr.prev
        elif c[0] == "D":
            for _ in range(int(c[2:])):
                curr = curr.next
        elif c[0] == "C":
            removed.append(curr)
            # 맨 앞 노드인 경우
            if not curr.prev:
                curr.next.prev = None
                curr = curr.next
            # 맨 뒤 노드인 경우
            elif not curr.next:
                curr.prev.next = None
                curr = curr.prev
            # 중간 노드인 경우
            else:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr = curr.next
        elif c[0] == "Z":
            restored = removed.pop()
            if restored.prev:
                restored.prev.next = restored
            if restored.next:
                restored.next.prev = restored

    # curr을 맨 앞으로 돌려놓기
    while curr.prev:
        curr = curr.prev

    # 최종결과 비교
    answer = ["X"] * n
    while curr:
        answer[curr.val] = "O"
        curr = curr.next
    return "".join(answer)
