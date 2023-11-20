class Node:
    def __init__(self, v):
        self.val = v
        self.prev = None
        self.next = None


def solution(n, k, cmd):
    # 연결리스트 생성
    head = cur = Node(0)
    for i in range(1, n):
        node = Node(i)
        cur.next = node
        node.prev = cur
        cur = cur.next

    # 초기 위치로 이동
    cur = head
    for _ in range(k):
        cur = cur.next

    # 삭제한 노드의 스택
    del_stack = []

    for c in cmd:
        if c[0] == "U":
            splt = c.split()
            for _ in range(int(splt[1])):
                cur = cur.prev
        elif c[0] == "D":
            splt = c.split()
            for _ in range(int(splt[1])):
                cur = cur.next
        elif c[0] == "C":
            # 맨 앞 노드인 경우
            if not cur.prev:
                cur.next.prev = None
                cur = cur.next
            # 맨 뒤 노드인 경우
            elif not cur.next:
                cur.prev.next = None
                cur = cur.prev
            # 중간 노드인 경우
            else:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur = cur.next
            del_stack.append(cur)
        elif c[0] == "Z":
            restored = del_stack.pop()
            if restored.prev:
                restored.prev.next = restored
            if restored.next:
                restored.next.prev = restored

    # cur을 맨 앞으로 돌려놓기
    while cur.prev:
        cur = cur.prev

    # 정답 구하기
    answer = ["X"] * n
    while cur:
        answer[cur.val] = "O"
        cur = cur.next
    return "".join(answer)


"""
- 분류: 자료구조 (연결리스트)
- 소요 시간:
    1:10-1:55 (45분) 구현 완료
    1:55-2:55 (60분) 디버깅

계획
- 양방향 연결리스트로 관리
- 삭제된 행은 스택으로 관리
- 삭제된 행은 어떻게 원래 위치로 복구? -> 어차피 복구는 역순이므로, 당시 정보 그대로 연결하면 됨
- 최종결과는 어떻게 정리? -> 앞에서부터 읽으면서 배열의 해당 위치에 O,X로 표시

디버깅
- 답이 틀림 or 런타임 에러
    - 1. 맨 앞 노드가 지워졌을때도 head에서부터 답을 찾는게 문제였음 (cur로 답을 찾도록 수정)
    - 2. 입력이 한자리수 이상이 될 수 있는데 split이 아닌 인덱스를 사용한게 문제였음 (와 레전드)
"""
