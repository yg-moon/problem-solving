# 마법사 상어와 파이어볼
from collections import defaultdict

N, M, K = map(int, input().split())
fireballs = [list(map(int, input().split())) for _ in range(M)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

dir1 = [0, 2, 4, 6]
dir2 = [1, 3, 5, 7]

# 핵심: {(x,y): [정보1, 정보2,...]}
cur_dic = defaultdict(list)
for x, y, m, s, d in fireballs:  # 주의: m, d, s 순서가 아님!
    cur_dic[(x, y)].append((m, s, d))  # 참고: 0-idx로 안 맞춰도 됨


def is_all_odd_or_all_even(lst):
    if all(x % 2 == 0 for x in lst) or all(x % 2 != 0 for x in lst):
        return True
    else:
        return False


for _ in range(K):
    # 이동
    moved_dic = defaultdict(list)
    for key in cur_dic:
        x, y = key
        for item in cur_dic[key]:
            m, s, d = item
            nx = (x + dx[d] * s) % N
            ny = (y + dy[d] * s) % N
            moved_dic[(nx, ny)].append((m, s, d))

    # 합체
    nxt_dic = defaultdict(list)
    for key in moved_dic:
        if len(moved_dic[key]) >= 2:  # 주의: "이동이 끝난 뒤 2개 이상이 있는 칸에서만"
            x, y = key
            m_sum = 0
            s_sum = 0
            d_lst = []
            # 더하기
            for item in moved_dic[key]:
                m, s, d = item
                m_sum += m
                s_sum += s
                d_lst.append(d)
            # 새 정보
            m_new = m_sum // 5
            s_new = s_sum // len(moved_dic[key])
            if is_all_odd_or_all_even(d_lst):
                dir = dir1
            else:
                dir = dir2
            # 추가하기
            if m_new > 0:
                for d_new in dir:
                    nxt_dic[(x, y)].append((m_new, s_new, d_new))
        else:
            nxt_dic[key] = moved_dic[key]

    cur_dic = nxt_dic

answer = 0
for key in cur_dic:
    for item in cur_dic[key]:
        m, s, d = item
        answer += m
print(answer)

"""
- 난이도: 골드4
- 분류: 시뮬레이션
- 소요 시간: 70분 (풀이 40분, 디버깅 30분)

요약
- 시키는대로 구현하는 문제
- 핵심: 좌표에 따른 파이어볼의 정보를 해시맵으로 관리 (cur_dic, moved_dic, nxt_dic)

디버깅: 답이 틀림
- 이유: 입력이 m, s, d 순서로 주어지는데 지문만 읽고 m, d, s로 착각했음

조건 정리
- 1행-N행, 1열-N열은 연결되어 있음
- 파이어볼은 (위치, 질량, 방향, 속력)이 있음
- 이동 -> 합체 -> 분리 -> 소멸
"""
