# 0시0분0초 ~ h시m분s초에 만나는 횟수를 계산
def calc_cnt(h, m, s):
    # 기본: 일단 1분에 2번씩 만남
    ret = (h * 60 + m) * 2

    # 예외1. 59분 -> 00분일때 분침과 만나지 않음
    ret -= h

    # 예외2. 11시 -> 12시일때 시침과 만나지 않음 (+ 정오에 겹치는 경우도 제외)
    if h >= 12:
        ret -= 2

    # 현재 시각의 각도
    h_deg = (h * 30 + m * 0.5 + s * 0.5 / 60) % 360
    m_deg = (m * 6 + s * 0.1) % 360
    s_deg = s * 6

    # 마지막 1분의 상태를 계산
    if s_deg >= m_deg:
        ret += 1
    if s_deg >= h_deg:
        ret += 1

    return ret


def solution(h1, m1, s1, h2, m2, s2):
    # (0:0:0 ~ h2:m2:s2 횟수) - (0:0:0 ~ h1:m1:s1 횟수)
    answer = calc_cnt(h2, m2, s2) - calc_cnt(h1, m1, s1)

    # 예외3. 0:0:0, 12:0:0
    if (h1 == 0 or h1 == 12) and m1 == 0 and s1 == 0:
        answer += 1

    return answer


"""
- 난이도: Lv2
- 분류: 수학

요약
- 기본적으로 1분에 초침이 한바퀴를 돌며 시침, 분침을 한번씩 만남 (1분당 *2번)
    - 예외1. 59분 → 00분에서 분침과 만나지 않음 (1시간당 -1번)
    - 예외2. 11시 → 12시에서 시침과 만나지 않음 (12시 넘으면 -1번)
    - 예외3. 0시0분0초, 12시0분0초에서 모두 동시에 겹침

- 출처: https://school.programmers.co.kr/questions/63464
"""
