from collections import deque


def solution(priorities, location):
    q = deque([(idx, pri) for idx, pri in enumerate(priorities)])  # [(인덱스1, 중요도1), ...]
    max_pri = max([pri for _, pri in q])
    print_cnt = 1

    while q:
        # 현재 문서의 중요도가 가장 높다면
        if q[0][1] >= max_pri:
            # 내가 찾는 문서였다면 인쇄 순서를 리턴
            if q[0][0] == location:
                return print_cnt
            # 다른 문서였다면 인쇄하여 대기목록에서 제거하고, 최대 중요도를 재계산
            else:
                q.popleft()
                print_cnt += 1
                max_pri = max([pri for _, pri in q])
        # 중요도가 더 높은 문서가 있다면 대기목록 맨 뒤로 보내기
        else:
            q.append(q.popleft())
