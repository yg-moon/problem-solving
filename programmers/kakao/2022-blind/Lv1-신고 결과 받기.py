from collections import defaultdict


def solution(id_list, report, k):
    user_to_list = defaultdict(list)
    user_to_cnt = defaultdict(int)

    for r in report:
        r = r.split()
        # 기존에 신고한 기록이 없을때만 처리
        if r[1] not in user_to_list[r[0]]:
            user_to_list[r[0]].append(r[1])
            user_to_cnt[r[1]] += 1

    answer = []
    for id in id_list:
        cnt = 0
        for user in user_to_list[id]:
            if user_to_cnt[user] >= k:
                cnt += 1
        answer.append(cnt)

    return answer
