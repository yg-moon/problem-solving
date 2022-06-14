import collections


def solution(id_list, report, k):
    user_to_report_list = collections.defaultdict(list)
    user_to_report_count = collections.defaultdict(int)

    for r in report:
        r = r.split()
        # 기존에 신고한 기록이 없을때만 처리
        if r[1] not in user_to_report_list[r[0]]:
            user_to_report_list[r[0]].append(r[1])
            user_to_report_count[r[1]] += 1

    answer = []
    for id in id_list:
        count = 0
        for user in user_to_report_list[id]:
            if user_to_report_count[user] >= k:
                count += 1
        answer.append(count)

    return answer
