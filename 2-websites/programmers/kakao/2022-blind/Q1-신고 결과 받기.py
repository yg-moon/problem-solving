from collections import defaultdict


def solution(id_list, report, k):
    info_dic = defaultdict(list)  # {유저: [자신이 신고한 유저들]}
    cnt_dic = defaultdict(int)  # {유저: 신고당한 횟수}
    answer = []

    for r in set(report):  # 주의: 중복 신고는 1회로 처리
        id1, id2 = r.split()
        info_dic[id1].append(id2)
        cnt_dic[id2] += 1

    for id1 in id_list:
        cnt = 0
        for id2 in info_dic[id1]:
            if cnt_dic[id2] >= k:
                cnt += 1
        answer.append(cnt)

    return answer


"""
- 분류: 구현, 해시
- 소요 시간: 10분
"""
