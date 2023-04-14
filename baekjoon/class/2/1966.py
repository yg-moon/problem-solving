# 프린터 큐
from collections import deque

answer = []

TC = int(input())

for _ in range(TC):
    N, target = map(int, input().split())
    doc_list = deque((range(N)))
    pri_list = deque((map(int, input().split())))
    max_pri = max(pri_list)
    print_cnt = 1

    while doc_list:
        # 현재 문서의 중요도가 가장 높다면
        if pri_list[0] == max_pri:
            # 내가 찾는 문서였다면 인쇄 순서를 정답에 기록
            if doc_list[0] == target:
                answer.append(print_cnt)
                break
            # 다른 문서였다면 인쇄하여 대기목록에서 제거하고, 최대 중요도를 재계산
            else:
                doc_list.popleft()
                pri_list.popleft()
                print_cnt += 1
                max_pri = max(pri_list)
        # 중요도가 더 높은 문서가 있다면 현재 문서를 대기목록 맨 뒤로 보내기
        else:
            doc_list.append(doc_list.popleft())
            pri_list.append(pri_list.popleft())

for a in answer:
    print(a)

"""
- 난이도: 실버3
- 분류: 큐, 시뮬레이션
"""
