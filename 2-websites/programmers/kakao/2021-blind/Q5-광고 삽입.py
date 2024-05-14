def to_sec(time):
    h, m, s = time.split(":")
    return (int(h) * 60 * 60) + (int(m) * 60) + int(s)


def to_time(sec):
    div, s = divmod(sec, 60)
    h, m = divmod(div, 60)
    h, m, s = str(h), str(m), str(s)
    result = []
    for x in [h, m, s]:
        if len(x) < 2:
            x = "0" + x
        result.append(x)
    return ":".join(result)


def solution(play_time, adv_time, logs):
    play_sec = to_sec(play_time)
    adv_sec = to_sec(adv_time)
    psum = [0] * (play_sec + 1)

    for log in logs:
        time1, time2 = log.split("-")
        # 효율성: 시작점과 끝점에만 표시
        # 현재 psum의 의미: 변화량
        psum[to_sec(time1)] += 1
        psum[to_sec(time2)] -= 1

    # 누적합 생성
    # 현재 psum의 의미: 누적량
    for i in range(1, play_sec + 1):
        psum[i] += psum[i - 1]

    max_cnt = sum(psum[:adv_sec])
    cur_cnt = max_cnt
    answer_sec = 0

    for sec in range(1, play_sec - adv_sec + 1):
        # 다음 상태 = 현재 상태 + 늘어난 값 - 줄어든 값
        cur_cnt += psum[sec + adv_sec - 1] - psum[sec - 1]
        if cur_cnt > max_cnt:
            max_cnt = cur_cnt
            answer_sec = sec

    return to_time(answer_sec)


"""
- 분류: 누적합

핵심
- 1. 초단위로 변환해서 배열에 표현
- 2. 누적합 응용
    - 변화량 추적: 모든 칸에 1을 더하는게 아니라, 시작점과 끝점에 1, -1을 써주기
    - 누적량 계산: 다음 상태 = 현재 상태 + 늘어난 값 - 줄어든 값
"""
