from collections import defaultdict
import math


def calc_diff(time1, time2):
    diff = 0
    h1, m1 = time1.split(":")
    h2, m2 = time2.split(":")
    diff += int(h1) * 60 + int(m1)
    diff -= int(h2) * 60 + int(m2)
    return diff


def solution(fees, records):
    total_time_dic = defaultdict(int)  # {차량: 누적 시간}
    in_time_dic = defaultdict(str)  # {차량: 들어온 시간}
    answer = []

    # 누적 시간 계산
    for record in records:
        time, car, inout = record.split()
        if inout == "IN":
            in_time_dic[car] = time
        elif inout == "OUT":
            in_time = in_time_dic[car]
            in_time_dic[car] = ""
            total_time_dic[car] += calc_diff(time, in_time)

    # 자정까지 안나간 차 계산
    for car in in_time_dic:
        if in_time_dic[car] != "":
            total_time_dic[car] += calc_diff("23:59", in_time_dic[car])

    # 주차요금 계산
    for car in sorted(total_time_dic.keys()):
        fee = fees[1]
        total_time = total_time_dic[car]
        if total_time > fees[0]:
            total_time -= fees[0]
            fee += math.ceil(total_time / fees[2]) * fees[3]
        answer.append(fee)

    return answer


"""
- 분류: 구현, 해시
- 소요 시간: 35분

요약
- 차량별 누적시간 계산
- 누적시간에 대해 요금 계산

자료구조
- {차량: 누적시간}
- {차량: 들어온 시간}
    - OUT을 만나면 현재있는 시간과 계산 후 빈칸으로 처리
    - 마지막에 한번 더 도는데 빈칸이 아니라면 23:59로 계산

팁
- 시간 계산은 분 단위로 통일해서 간편하게 처리
"""
